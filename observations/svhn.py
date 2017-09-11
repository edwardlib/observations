from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def svhn(path, load_extra=False):
  """Load the Street View House Numbers data set in cropped digits
  format [@netzer2011reading]. It consists of 32x32 RGB images in 10
  classes. There are 73257 training images, 26032 test images, and
  531131 extra images.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filenames are
      `train_32x32.mat`, `test_32x32.mat`, `extra_32x32.mat`.
    load_extra: bool, optional.
      Whether to load the extra images. Default is False.

  Returns:
    Tuple of np.ndarray's
    `(x_train, y_train), (x_test, y_test)`, and a third tuple of
    `(x_extra, y_extra)` if `load_extra` is True.
  """
  from scipy.io import loadmat
  path = os.path.expanduser(path)
  url = 'http://ufldl.stanford.edu/housenumbers/'
  train = 'train_32x32.mat'
  test = 'test_32x32.mat'
  if not os.path.exists(os.path.join(path, train)):
    maybe_download_and_extract(path, url + train)
  if not os.path.exists(os.path.join(path, test)):
    maybe_download_and_extract(path, url + test)

  loaded = loadmat(os.path.join(path, train))
  x_train = loaded['X'].transpose(3, 0, 1, 2)
  y_train = loaded['y'].flatten()
  y_train[y_train == 10] = 0

  loaded = loadmat(os.path.join(path, test))
  x_test = loaded['X'].transpose(3, 0, 1, 2)
  y_test = loaded['y'].flatten()
  y_test[y_test == 10] = 0

  if load_extra:
    extra = 'extra_32x32.mat'
    if not os.path.exists(os.path.join(path, extra)):
      maybe_download_and_extract(path, url + extra)
    loaded = loadmat(os.path.join(path, extra))
    x_extra = loaded['X'].transpose(3, 0, 1, 2)
    y_extra = loaded['y'].flatten()
    y_extra[y_extra == 10] = 0
    return (x_train, y_train), (x_test, y_test), (x_extra, y_extra)
  else:
    return (x_train, y_train), (x_test, y_test)
