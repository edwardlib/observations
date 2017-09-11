from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def abalone(path):
  """Load the Abalone data set [@nash1994population].
  It contains 4,177 examples of abalones with nine measured attributes
  such as sex, length, diameter, and whole weight. The first column
  (sex) is encoded as 0 for M (male), 1 for F (female), 2 for I
  (infant).

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `housing.data`.

  Returns:
    Tuple of np.darray `x_train` with 4,177 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = 'abalone.data'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/' \
          'abalone/abalone.data'
    maybe_download_and_extract(path, url)

  encoder = {'M': 0, 'F': 1, 'I': 2}
  with open(os.path.join(path, filename)) as f:
    iterator = csv.reader(f)
    x_train = []
    for row in iterator:
      row[0] = encoder[row[0]]
      x_train.append(row)
  x_train = np.array(x_train, dtype=np.float)
  columns = ['sex',
             'length',
             'diameter',
             'height',
             'whole weight',
             'shucked weight',
             'viscera weight',
             'shell weight',
             'rings']
  metadata = {'columns': columns}
  return x_train, metadata
