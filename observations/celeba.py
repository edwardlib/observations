from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os
import zipfile


def celeba(path):
  """Load the Large-scale CelebFaces Attributes (CelebA) data set (Liu
  et al., 2015). It consists of ~200,000 178x218 RGB images, each with
  40 annotated attributes, and with a total of ~10,000 identities.
  Here we load only the images.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `img_align_celeba/`.

  Returns:
    str. It is a message advising to load data manually.
  """
  import requests
  from tqdm import tqdm
  def _maybe_download_and_extract(path, url, drive_id):
    if not os.path.exists(path):
      session = requests.Session()
      response = session.get(url, params={'id': drive_id}, stream=True)
      token = None
      for key, value in response.cookies.items():
        if key.startswith('download_warning'):
          token = value
      if token:
        response = session.get(
            url, params={'id': drive_id, 'confirm': token}, stream=True)
      total_size = int(response.headers.get('content-length', 0))
      chunk_size = 32 * 1024
      with open(destination, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size), total=total_size,
                          unit='B', unit_scale=True, desc=destination):
          if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    with zipfile.ZipFile(path) as f:
      f.extractall(path)
  path = os.path.expanduser(path)
  if not os.path.exists(os.path.join(path, 'img_align_celeba')):
    save_path = os.path.join(path, 'img_align_celeba.zip')
    url = 'https://docs.google.com/uc?export=download'
    drive_id = '0B7EVK8r0v71pZjFTYXZWM3FlRnM'
    _maybe_download_and_extract(save_path, url, drive_id)
  string = "Data set is larger than 1 GB. We recommend loading your " \
           "data in batches."
  return string
