from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os
import six
import sys

from observations.util import maybe_download_and_extract
from six.moves import cPickle


def cifar100(path, label_mode='fine'):
  """Load the CIFAR-100 data set [@krizhevsky2009learning].
  It consists of 32x32 RGB images in 100 classes, with 600 images per
  class. There are 500 training images and 100 testing images per
  class.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `cifar-100-python/`.
    label_mode: str.
      'fine' (class to which image belongs) or 'coarse' (superclass to
      which image belongs).

  Returns:
    Tuple of np.ndarray's
    `(x_train, y_train), (x_test, y_test)`.
  """
  def _load_batch(filepath, label_key):
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
    labels = d[label_key]
    images = images.reshape(images.shape[0], 3, 32, 32)
    labels = np.reshape(labels, len(labels,))
    return images, labels
  path = os.path.expanduser(path)
  directory = 'cifar-100-python'
  if not os.path.exists(os.path.join(path, directory)):
    url = 'http://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz'
    maybe_download_and_extract(path, url)

  filepath = os.path.join(path, directory, 'train')
  x_train, y_train = _load_batch(filepath, label_mode + '_labels')

  filepath = os.path.join(path, directory, 'test')
  x_test, y_test = _load_batch(filepath, label_mode + '_labels')
  return (x_train, y_train), (x_test, y_test)
