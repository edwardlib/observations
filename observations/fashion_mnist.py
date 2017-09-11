from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np

from observations.util import maybe_download_and_extract


def fashion_mnist(path):
  """Load the Fashion MNIST data set [@xiao2017fashion].

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filenames are
      `train-images-idx3-ubyte`, `train-labels-idx1-ubyte`,
      `t10k-images-idx3-ubyte`, `t10k-labels-idx1-ubyte`.

  Returns:
    Tuple of np.ndarray's
    `(x_train, y_train), (x_test, y_test)`.
  """
  path = os.path.expanduser(path)
  url = 'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/'
  train_images = 'train-images-idx3-ubyte'
  train_labels = 'train-labels-idx1-ubyte'
  test_images = 't10k-images-idx3-ubyte'
  test_labels = 't10k-labels-idx1-ubyte'

  if not os.path.exists(os.path.join(path, train_images)):
    maybe_download_and_extract(path, url + train_images + '.gz')
  if not os.path.exists(os.path.join(path, train_labels)):
    maybe_download_and_extract(path, url + train_labels + '.gz')
  if not os.path.exists(os.path.join(path, test_images)):
    maybe_download_and_extract(path, url + test_images + '.gz')
  if not os.path.exists(os.path.join(path, test_labels)):
    maybe_download_and_extract(path, url + test_labels + '.gz')

  with open(os.path.join(path, train_images)) as f:
    loaded = np.fromfile(file=f, dtype='uint8')
  x_train = loaded[16:].reshape((60000, 28 * 28)).astype(float)
  with open(os.path.join(path, train_labels)) as f:
    loaded = np.fromfile(file=f, dtype='uint8')
  y_train = loaded[8:].reshape((60000,))
  with open(os.path.join(path, test_images)) as f:
    loaded = np.fromfile(file=f, dtype='uint8')
  x_test = loaded[16:].reshape((10000, 28 * 28)).astype(float)
  with open(os.path.join(path, test_labels)) as f:
    loaded = np.fromfile(file=f, dtype='uint8')
  y_test = loaded[8:].reshape((10000,))

  return (x_train, y_train), (x_test, y_test)
