from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os
import six
import sys

from observations.util import maybe_download_and_extract
from six.moves import cPickle


def cifar10(path):
  """Load the CIFAR-10 data set [@krizhevsky2009learning].
  It consists of 32x32 RGB images in 10 classes, with 6000 images per
  class. There are 50000 training images and 10000 test images.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `cifar-10-batches-py/`.

  Returns:
    Tuple of np.ndarray's
    `(x_train, y_train), (x_test, y_test)`.
  """
  def _load_batch(filepath):
    with open(filepath, 'rb') as f:
      if sys.version_info < (3,):
        d = cPickle.load(f)
      else:
        d = cPickle.load(f, encoding='bytes')
        d_decoded = {}  # decode utf8
        for k, v in six.iteritems(d):
          d_decoded[k.decode('utf8')] = v
        d = d_decoded
    images = d['data']
    labels = d['labels']
    images = images.reshape(images.shape[0], 3, 32, 32)
    labels = np.reshape(labels, len(labels,))
    return images, labels
  path = os.path.expanduser(path)
  directory = 'cifar-10-batches-py'
  if not os.path.exists(os.path.join(path, directory)):
    url = 'http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    maybe_download_and_extract(path, url)

  path = os.path.join(path, directory)
  x_train = np.zeros((50000, 3, 32, 32), dtype='uint8')
  y_train = np.zeros((50000,), dtype='uint8')
  for i in range(1, 6):
    filepath = os.path.join(path, 'data_batch_' + str(i))
    images, labels = _load_batch(filepath)
    x_train[(i - 1) * 10000: i * 10000, :, :, :] = images
    y_train[(i - 1) * 10000: i * 10000] = labels

  filepath = os.path.join(path, 'test_batch')
  x_test, y_test = _load_batch(filepath)
  return (x_train, y_train), (x_test, y_test)
