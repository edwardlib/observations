from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import hashlib
import math
import os
import requests
import shutil
import sys
import tarfile
import time
import zipfile

from six.moves import urllib


def _get_google_confirm_id_token(url, session):
  """Helper function to get confirmation token for Google Drive.

  Args:
    url: str.
      URL string to the file.
    session: object.
      Session to get the cookie token.

  Returns:
    (str,str). (Resource id of the google file, confirmation token).
  """
  parse_results = urllib.parse.parse_qs(url)
  try:
    file_id = parse_results['id'][0]
    response = session.get(url, params={'id': file_id}, stream=True)
    for key, value in response.cookies.items():
      if key.startswith('download_warning'):
        return file_id, value
    return file_id, None
  except KeyError:
    return None, None


def _gdrive_params(url, session):
  """Helper function returning Google Drive specific parameters.

    Args:
      url: str.
        URL string to the file.
      session: object.
        Session to get the cookie token.

    Returns:
      dict of id & confirmation token parameters required for GET
      request to Google Drive resource.
    """
  params = {}
  file_id, token = _get_google_confirm_id_token(url, session)
  if file_id is not None:
    params['id'] = file_id
  if token is not None:
    params['confirm'] = token
  return params


def _print_capabilities(cap_dict):
  """Helper function to print capabilities of a given URL.

  Args:
    cap_dict: dict.
      Capabilities dictionary object.
  """
  print("Content Type:         [{}] ".format(cap_dict['content_type']))
  print("Supports Resume:      [{}] ".format('Y'
                                             if cap_dict['supports_resume']
                                             else 'N'))
  print("Supports File Size:   [{}] ".format('Y'
                                             if cap_dict['supports_file_size']
                                             else 'N'))
  print("File Size:            [{}] ".format(cap_dict['file_size']))
  print("Additional GET params [{}]".format(cap_dict['addnl_params']))


def check_capabilities(url, start=120, num_bytes=300, user_agent=None,
                       _print=True):
  """Check capabilities of a specified URL. This function queries the URL
  to get a response on the remote server capabilities. Requests for `num_bytes`
  bytes of data to check `total_file_size`, range support, Google
  Drive specific params.

  Args:
    url: str.
      URL string to the file.
    start: int, optional.
      Start position of the bytes of the file requested.
    num_bytes: int, optional.
      Number of bytes from the start byte requested.
    user_agent: str, optional.
      User agent which is sometimes required to query some domains for proper
      download.
    _print: bool, optional.
     Print the remote server capabilities.

  Returns
    dict of remote server capabilities, required prior to full
    download.
  """
  supports_resume = False
  supports_file_size = False
  user_agent_default = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0' \
                       ') Gecko/20100101 Firefox/32.0'
  user_agent = user_agent_default if user_agent is None else user_agent
  params = {}
  session = requests.Session()
  if 'drive.google.com' in url or 'docs.google.com' in url:
    params = _gdrive_params(url, session)
  range_header = {'User-Agent': user_agent,
                  'Range': 'bytes=%d-%d' % (start, start + num_bytes)}
  response = session.get(url, headers=range_header, params=params, stream=True)
  content_type = response.headers.get('content-type')
  try:
    num_bytes_in_range = int(response.headers.get('content-length'))
    if num_bytes_in_range == num_bytes + 1:
      supports_resume = True
    else:
      supports_resume = False
  except TypeError:
    supports_resume = False
  try:
    file_size = int(response.headers.get('content-range').split('/')[1])
    supports_file_size = True
  except TypeError:
    file_size = 0
    supports_file_size = False
  capabilities_dict = {'content_type': content_type,
                       'supports_resume': supports_resume,
                       'supports_file_size': supports_file_size,
                       'file_size': file_size,
                       'addnl_params': params,
                       'user_agent': user_agent,
                       'session': session
                       }
  if _print:
    _print_capabilities(capabilities_dict)
  return capabilities_dict


def humanize_size(n):
  """Convert file size in bytes to a friendly human readable form.

  Args:
    n: int.
      Size in bytes.

  Returns:
    str. Human-friendly size.

  #### Examples

  ```python
  humanize_size(1024)
  ## '1 KB'
  ```
  """
  exp = 0
  b = 1024
  u = 'B'
  pre = [''] + [p + '' for p in 'KMGTPEZY']
  r, f = min(int(math.log(max(n * b ** exp, 1), b)),
             len(pre) - 1), '{:,.%if} %s%s'
  h = (f % (abs(r % (-r - 1)), pre[r], u)).format(n * b ** exp / b ** float(r))
  return h


def humanize_time(duration, fmt_short=True):
  """Convert duration in seconds to a friendly human readable form.

  Args:
    duration: int.
      Duration in seconds.
    fmt_short: bool, optional.
      Display output in short/long format.

  Returns:
    str. Human-friendly durations.

  #### Examples

  ```python
  humanize_time(3662)
  ## '1h 1m 2s'

  humanize_time(3662, fmt_short=False)
  ## '1 hour, 1 minute, 2 seconds'
  ```
  """
  duration = int(duration)
  if duration == 0:
    return "0s" if fmt_short else "0 seconds"

  intervals = [1, 60, 3600, 86400, 604800, 2419200, 29030400]
  if fmt_short:
    names = ['s' * 2, 'm' * 2, 'h' * 2, 'd' * 2, 'w' * 2, 'y' * 2]
  else:
    names = [('second', 'seconds'),
             ('minute', 'minutes'),
             ('hour', 'hours'),
             ('day', 'days'),
             ('week', 'weeks'),
             ('month', 'months'),
             ('year', 'years')]

  result = []

  for i in range(len(names) - 1, -1, -1):
    a = duration // intervals[i]
    if a > 0:
      result.append((a, names[i][1 % a]))
      duration -= a * intervals[i]

  if fmt_short:
    return " ".join(["%s%s" % x for x in result])
  return ", ".join(["%s %s" % x for x in result])


def get_file_size(url, params, timeout=10):
  """Get file size from a given URL in bytes.

  Args:
    url: str.
      URL string.
    timeout: int, optional.
      Timeout in seconds.

  Returns:
    int. File size in bytes.

  #### Examples

  ```python
  get_file_size(url)
  ## 178904
  ```
  """
  try:
    response = requests.get(url, params={}, stream=True)
  except (requests.exceptions.HTTPError) as e:
    print(e)
    return 0
  try:
    file_size = int(response.headers["Content-Length"])
  except (IndexError, KeyError, TypeError):
    return 0

  return file_size


def get_file_hash(path, algorithm='md5'):
  """Get hash from a given file and hashing algorithm.

  Args:
    path: str.
      Full path to a file.
    algorithm: str, optional.
      Name of hashing algorithm. See `hashlib.algorithms_available`
      for list of available hashing algorithms in python.

  Returns:
    str. File hash computed from the file using the specified algorithm.

  #### Examples

  ```python
  get_file_hash('train.gz')
  ## '5503d900f6902c61682e6b6f408202cb'
  ```
  """
  hash_alg = hashlib.new(algorithm)
  with open(path, 'rb') as f:
    read_size = 1024 * 1024 * 4
    data = f.read(read_size)
    while data:
      hash_alg.update(data)
      data = f.read(read_size)
  return hash_alg.hexdigest()


def hashes_match(path, hash_true, algorithm='md5'):
  """Check whether the computed hash from the file matches the
  specified hash string.

  Args:
    path: str.
      Full path to a file.
    hash_true: str.
      True hash of the file.
    algorithm: str, optional.
      Name of hashing algorithm. See `hashlib.algorithms_available`
      for list of available hashing algorithms in python.

  Returns:
    bool. True if the hashes match, else False.

  #### Examples

  ```python
  hashes_match('train.gz', '5503d900f6902c61682e6b6f408202cb')
  ## True
  ```
  """
  if os.path.exists(path):
    return get_file_hash(path, algorithm) == hash_true
  else:
    return False


def check_file_downloaded(file_path, file_size):
  """Check whether a file of specified size exists.

  Args:
    file_path: str.
      Full path of the file.
    file_size: int.
      Size of the file in bytes.

  Returns:
    bool. True if file with specified size exists.
  """
  file_exists = os.path.exists(file_path)
  local_file_size = os.path.getsize(file_path) if file_exists else -1
  if file_size == local_file_size:
    return True
  else:
    return False


def _print_progress(file_path, dl_bytes, file_size, block_size, count,
                    _start_time):
  """Helper function that is called to print progress of download.

  Args:
    file_path: str.
      Full path of the file.
    dl_bytes: int.
      Bytes already downloaded in bytes.
    file_size. int.
      Total file size in bytes.
    block_size: int.
      Block size of bytes requested per iteration.
    count: int.
      Iteration count.
    _start_time: object.
      Time object to indicate when download started.

  Returns:
    None.
  """
  if file_size > 0:
    percent = math.floor(dl_bytes / file_size * 100)
    duration = time.time() - _start_time
    progress_size = min(dl_bytes, file_size)
    remaining_size = file_size - progress_size
    speed = math.floor(count * block_size / duration)
    eta = math.ceil(remaining_size / speed)
    eta = eta if eta >= 0 else 0
    o_str = '\r>> [%s/%s] %d%% @%s/s,[%s remaining, %s elapsed]        '
    sys.stdout.write(o_str % (
                     humanize_size(progress_size),
                     humanize_size(file_size),
                     percent,
                     humanize_size(speed),
                     humanize_time(eta),
                     humanize_time(duration)))
    sys.stdout.flush()
  else:
    duration = time.time() - _start_time
    speed = math.floor(count * block_size / duration)
    progress_size = dl_bytes
    o_str = '\r>> [%s/%s] @%s/s,[%s elapsed]        '
    sys.stdout.write(o_str % (
                     humanize_size(progress_size),
                     'Unknown',
                     humanize_size(speed),
                     humanize_time(duration)))
    sys.stdout.flush()


def normal_download(url, file_path, session, params=None, headers=None,
                    hash_true=None, timeout=10, block_size=1024 * 1024):
  """Start download of a file. No pause/resume capability.

  Args:
    url: str.
      URL string to the file.
    file_path: str.
      Full path to filename to be saved locally.
    session: object.
      The current session in use.
    params: dict, optional.
      Additional params that are passed to session.
    headers: dict, optional.
      Header information passed to session.
    hash_true: str, optional.
      True hash string of the requested file.
    timeout: int, optional.
      Timeout in secs.
    block_size: int, optional.
      Block size in bytes to be read.

  Returns:
    bool. True if file is successfully downloaded.
  """
  if params is None:
    params = {}
  if headers is None:
    headers = {}
  file_size = get_file_size(url, timeout)
  if check_file_downloaded(file_path, file_size):
    print('File [{}] with same size already downloaded & '
          'exists in the provided path'.format(file_path))
    return True
  else:
    try:
      print('>> Downloading {}' . format(file_path))
      response = session.get(url,
                             params=params,
                             headers=headers,
                             stream=True)
      with open(file_path, 'wb') as f:
        start_time = time.time()
        count = 1
        for chunk in response.iter_content(block_size):
          if chunk:
            f.write(chunk)
            f.flush()
            _print_progress(file_path, count * block_size, file_size,
                            block_size, count, start_time)
            count = count + 1
      if file_size == os.path.getsize(file_path):
        if hash_true is not None and not hashes_match(file_path,
                                                      hash_true):
          raise Exception('Error validating the file '
                          'against its MD5 hash')
        if hash_true is None:
          print("\nURL {} downloaded to {} ".format(url, file_path))
        else:
          print("\nURL {} downloaded to {} and hash verified "
                "succesfully".format(url, file_path))
        return True
    except:
      if os.path.exists(file_path):
        os.remove(file_path)
      raise


def download_file(url, file_path, hash_true=None, resume=True,
                  block_size=1024 * 1024):
  """Start or resume partially downloaded file from specified URL.

  Args:
    url: str.
      URL string to the file.
    file_path: str.
      Full path to filename to be saved locally.
    hash_true: str, optional.
      True hash string of the requested file.
    resume: bool, optional.
      Resumes a file from current partially saved state [filename.part].
    block_size: int, optional.
      Number of bytes requested per range request. Setting this seems to be
      an art. The defaults work for many cases.

  Returns:
    bool. True if file is successfully downloaded.
  """
  response_check = check_capabilities(url, _print=False)
  file_size = response_check['file_size']
  params = response_check['addnl_params']
  content_length_file_size = get_file_size(url, params)
  user_agent = response_check['user_agent']
  session = response_check['session']
  if resume:
    supports_resume = response_check['supports_resume']
    # If file size mismatch occurs, something is wrong
    # Server sends content-size that is misleading
    if (content_length_file_size != 0) and \
       (file_size == 0 or file_size != content_length_file_size):
      file_size = content_length_file_size
      supports_resume = False
  else:
    supports_resume = False
  # If we cannot trust support_resume claims from server or user
  # does not want resume capability revert to normal download
  # NOTE: Always set resume=False for Github raw urls that
  # serves csv/notebooks.
  if not supports_resume:
    return normal_download(url, file_path, session,
                           params=params,
                           headers={'User-Agent': user_agent},
                           hash_true=hash_true,
                           block_size=block_size
                           )
  # Else perform multi-part download
  if check_file_downloaded(file_path, file_size):
    print('File [{}] with same size already downloaded & '
          'exists in the provided path'.format(file_path))
    return True
  if supports_resume:
    tmp_file_path = file_path + '.part'
    tmp_file_exists = os.path.exists(tmp_file_path)
    start_byte = os.path.getsize(tmp_file_path) if tmp_file_exists else 0
  else:
    tmp_file_path = file_path
    if os.path.exists(tmp_file_path + '.part'):
      os.remove(tmp_file_path + '.part')
    start_byte = 0
  if start_byte > 0:
    print('>> Resuming Download of {} from {}'
          ' onwards'.format(tmp_file_path, humanize_size(start_byte)))
  else:
    print('>> Downloading {}'
          ' '.format(tmp_file_path, humanize_size(start_byte)))
  try:
    start_time = time.time()
    count = 1
    headers = {'Range': 'bytes=%d-' % start_byte,
               'User-Agent': user_agent
               }
    response = session.get(url,
                           params=params,
                           stream=True,
                           headers=headers)
    with open(tmp_file_path, 'ab') as f:
      for chunk in response.iter_content(block_size):
        if chunk:
          f.write(chunk)
          f.flush()
          _print_progress(tmp_file_path, start_byte + count * block_size,
                          file_size, block_size,
                          count, start_time)
          count = count + 1
  except IOError as e:
    print('IO Error - %s' % e)
    raise
  finally:
    # rename the temp download file to the correct name if fully downloaded
    if file_size == os.path.getsize(tmp_file_path):
      if hash_true is not None and not \
              hashes_match(tmp_file_path, hash_true):
        raise Exception('Error validating the file '
                        'against its MD5 hash')
      shutil.move(tmp_file_path, file_path)
      if hash_true is None:
        print("\nURL {} downloaded to {} ".format(url, file_path))
      else:
        print("\nURL {} downloaded to {} and hash verified "
              "succesfully".format(url, file_path))
      return True


def maybe_download_and_extract(path, url, extract=True,
                               hash_true=None, resume=True,
                               save_file_name=None):
  """Download file from url unless it already exists in specified directory.
  Extract the file if `extract` is True.

  The file at `url` is downloaded to the directory `path`
  with its original filename. For example, with url
  `http://example.org/example.txt` and path `~/data`, the
  downloaded file is located at `~/data/example.txt`.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
    url: str.
      URL to download from if file doesn't exist.
    extract: bool, optional.
      If True, tries to extract the file if it has format 'gz',
      'tar' (including 'tar.gz' and 'tar.bz'), or 'zip'.
    hash_true: str, optional.
      Hash (md5 or otherwise) string of the remote file to be downloaded.
    resume: bool, optional.
      If True, tries to resume partial downloads (if supported by server).
    save_file_name: str, optional.
      Save to specified file name, else derives from URL path.

  Returns:
    str. Path to downloaded or already existing file.
  """
  path = os.path.expanduser(path)
  if not os.path.exists(path):
    os.makedirs(path)
  if save_file_name is None:
    filename = url.split('/')[-1]
  else:
    filename = save_file_name
  filepath = os.path.join(path, filename)
  if os.path.exists(filepath):
    print('{} already exists'.format(filepath))
  else:
    download_file(url, filepath, hash_true, resume)

  if extract:
    if tarfile.is_tarfile(filepath):
      with tarfile.open(filepath) as f:
        f.extractall(path)
    elif filename.endswith('.gz'):
      with gzip.open(filepath, 'rb') as f:
        s = f.read()
      extracted_filepath = os.path.splitext(filepath)[0]
      with open(extracted_filepath, 'wb') as f:
        f.write(s)
    elif zipfile.is_zipfile(filepath):
      with zipfile.ZipFile(filepath) as f:
        f.extractall(path)

  return filepath
