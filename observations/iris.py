from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from observations.util import maybe_download_and_extract


def iris(path):
  """Load the Iris Plants data set (Fisher, 1936). It contains 150
  examples of iris plants, each with 4 continuous attributes and its
  class.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `iris.data`.

  Returns:
    np.darray `x_train, y_train`.
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'iris.data'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    maybe_download_and_extract(path, url)
  data = pd.read_csv(os.path.join(path, filename), header=None)
  class_index = data.shape[1] - 1
  x_train = data[range(class_index)].as_matrix()
  y_train = data[class_index].as_matrix().astype(str)
  return x_train, y_train
