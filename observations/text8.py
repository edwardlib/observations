from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def text8(path):
  """Load the text8 data set [@mahoney2006large].
  The dataset is preprocessed and has a vocabulary of 27 characters.
  There are 100 million characters.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `text8`.

  Returns:
    Tuple of str `x_train, x_test, x_valid`.
  """
  path = os.path.expanduser(path)
  filename = 'text8'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://mattmahoney.net/dc/text8.zip'
    maybe_download_and_extract(path, url)
  with open(os.path.join(path, filename)) as f:
    text = f.read()
  x_train = text[:int(90e6)]
  x_test = text[int(95e6):int(100e6)]
  x_valid = text[int(90e6):int(95e6)]
  return x_train, x_test, x_valid
