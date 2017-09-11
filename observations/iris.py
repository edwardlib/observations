from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def iris(path):
  """Load the Iris Plants data set [@fisher1936use].
  It contains 150 examples of iris plants, each with 4 real-valued
  attributes and its class.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `iris.data`.

  Returns:
    Tuple of np.darray `x_train`, np.ndarray `y_train`, and dictionary
    `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = 'iris.data'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/' \
          'iris/iris.data'
    maybe_download_and_extract(path, url)

  with open(os.path.join(path, filename)) as f:
    iterator = csv.reader(f)
    x_train = []
    y_train = []
    for row in iterator:
      if row:
        x_train.append(row[:-1])
        y_train.append(row[-1])
  x_train = np.array(x_train, dtype=np.float)
  y_train = np.array(y_train)
  columns = ['sepal length (cm)', 'sepal width (cm)',
             'petal length (cm)', 'petal width (cm)']
  metadata = {'columns': columns}
  return x_train, y_train, metadata
