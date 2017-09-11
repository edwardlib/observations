from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os

from observations.util import maybe_download_and_extract


def small64_imagenet(path):
  """Load the small 64x64 ImageNet data set [@vandenoord2016pixel].
  It consists of millions of 64x64 RGB images.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `imgnet_64x64.npz`.

  Returns:
    Tuple of np.ndarray's `x_train, x_test`.
  """
  from scipy.misc import imread
  path = os.path.expanduser(path)
  url = 'http://image-net.org/small/'

  npz_file = os.path.join(path, 'imgnet_64x64.npz')
  if not os.path.exists(npz_file):
    train = 'train_64x64'
    valid = 'valid_64x64'
    if not os.path.exists(os.path.join(path, train)):
      maybe_download_and_extract(path, url + train + '.tar')
    if not os.path.exists(os.path.join(path, valid)):
      maybe_download_and_extract(path, url + valid + '.tar')

    trainx = []
    train_dir = os.path.join(path, train)
    for f in os.listdir(train_dir):
      if f.endswith('.png'):
        print('reading', f)
        filepath = os.path.join(train_dir, f)
        trainx.append(imread(filepath).reshape((1, 64, 64, 3)))

    trainx = np.concatenate(trainx, axis=0)

    testx = []
    test_dir = os.path.join(path, valid)
    for f in os.listdir(test_dir):
      if f.endswith('.png'):
        print('reading', f)
        filepath = os.path.join(test_dir, f)
        testx.append(imread(filepath).reshape((1, 64, 64, 3)))

    testx = np.concatenate(testx, axis=0)
    np.savez(npz_file, trainx=trainx, testx=testx)

  imagenet_data = np.load(npz_file)
  x_train = imagenet_data['trainx']
  x_test = imagenet_data['testx']
  return x_train, x_test
