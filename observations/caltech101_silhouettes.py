from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def caltech101_silhouettes(path, resolution=28):
  """Load the Caltech 101 Silhouettes data set [@marlin2010inductive].
  It contains binarized 28x28 (or 14x14) pixel images of objects
  belonging to 101 categories. There are 4,100 examples in the
  training set, 2,264 examples in the validation set and 2,307
  examples in the test set.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filenames are
      `caltech101_silhouettes_28_split1.mat` if resolution is 28;
      else `caltech101_silhouettes_14_split1.mat`.
    resolution: int, optional.
      Resolution of pixel images, 14 or 28.

  Returns:
    Tuple of np.ndarray tuples, `(x_train, y_train)`, `(x_test,
    y_test)`, and `(x_valid, y_valid)`.
  """
  from scipy.io import loadmat
  if resolution == 28:
    filename = 'caltech101_silhouettes_28_split1.mat'
    url = 'http://people.cs.umass.edu/~marlin/data/' \
          'caltech101_silhouettes_28_split1.mat'
  else:
    filename = 'caltech101_silhouettes_16_split1.mat'
    url = 'http://people.cs.umass.edu/~marlin/data/' \
          'caltech101_silhouettes_16_split1.mat'
  path = os.path.expanduser(path)
  if not os.path.exists(os.path.join(path, filename)):
    maybe_download_and_extract(path, url)

  loaded = loadmat(os.path.join(path, filename))
  x_train = loaded['train_data']
  x_test = loaded['test_data']
  x_valid = loaded['val_data']
  y_train = loaded['train_labels']
  y_test = loaded['test_labels']
  y_valid = loaded['val_labels']
  return (x_train, y_train), (x_test, y_test), (x_valid, y_valid)
