from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os

from observations.util import maybe_download_and_extract
from observations.mnist import mnist


def multi_mnist(path, max_digits=2, canvas_size=50, seed=42):
  """Load the multiple MNIST data set [@eslami2016attend]. It modifies
  the original MNIST such that each image contains a number of
  non-overlapping random MNIST digits with equal probability.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is
      `'multi_mnist_{}_{}_{}.npz'.format(max_digits, canvas_size, seed)`.
    max_digits: int, optional.
      Maximum number of non-overlapping MNIST digits per image to
      generate if not cached.
    canvas_size: list of two int, optional.
      Width x height pixel size of generated images if not cached.
    seed: int, optional.
      Random seed to generate the data set from MNIST if not cached.

  Returns:
    Tuple of (np.ndarray of dtype uint8, list)
    `(x_train, y_train), (x_test, y_test)`. Each element in the y's is a
    np.ndarray of labels, one label for each digit in the image.
  """
  from scipy.misc import imresize
  def _sample_one(canvas_size, x_data, y_data):
    i = np.random.randint(x_data.shape[0])
    digit = x_data[i]
    label = y_data[i]
    scale = 0.1 * np.random.randn() + 1.3
    resized = imresize(digit, 1.0 / scale)
    width = resized.shape[0]
    padding = canvas_size - width
    pad_l = np.random.randint(0, padding)
    pad_r = np.random.randint(0, padding)
    pad_width = ((pad_l, padding - pad_l), (pad_r, padding - pad_r))
    positioned = np.pad(resized, pad_width, 'constant', constant_values=0)
    return positioned, label
  def _sample_multi(num_digits, canvas_size, x_data, y_data):
    canvas = np.zeros((canvas_size, canvas_size))
    labels = []
    for _ in range(num_digits):
      positioned_digit, label = _sample_one(canvas_size, x_data, y_data)
      canvas += positioned_digit
      labels.append(label)
    labels = np.array(labels, dtype=np.uint8)
    if np.max(canvas) > 255:  # crude check for overlapping digits
      return _sample_multi(num_digits, canvas_size, x_data, y_data)
    else:
      return canvas, labels
  def _build_dataset(x_data, y_data, max_digits, canvas_size):
    x = []
    y = []
    data_size = x_data.shape[0]
    data_num_digits = np.random.randint(max_digits + 1, size=data_size)
    x_data = np.reshape(x_data, [data_size, 28, 28])
    for num_digits in data_num_digits:
      canvas, labels = _sample_multi(num_digits, canvas_size, x_data, y_data)
      x.append(canvas)
      y.append(labels)
    x = np.array(x, dtype=np.uint8)
    return x, y
  path = os.path.expanduser(path)
  cache_filename = 'multi_mnist_{}_{}_{}.npz'.format(
      max_digits, canvas_size, seed)
  if os.path.exists(os.path.join(path, cache_filename)):
    data = np.load(os.path.join(path, cache_filename))
    return (data['x_train'], data['y_train']), (data['x_test'], data['y_test'])

  np.random.seed(seed)
  (x_train, y_train), (x_test, y_test) = mnist(path)
  x_train, y_train = _build_dataset(x_train, y_train, max_digits, canvas_size)
  x_test, y_test = _build_dataset(x_test, y_test, max_digits, canvas_size)
  with open(os.path.join(path, cache_filename), 'wb') as f:
    np.savez_compressed(f, x_train=x_train, y_train=y_train,
                        x_test=x_test, y_test=y_test)
  return (x_train, y_train), (x_test, y_test)
