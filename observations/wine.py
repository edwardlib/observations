from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os

from observations.util import maybe_download_and_extract


def wine(path):
  """Load the wine data set [@forina1991extendible].
  It contains 178 examples of wines grown in the same region in Italy
  but derived from three different cultivars (first column). Each
  example has 13 integer-valued and continuous attributes such as
  alcohol, malic acid, and ash.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `wine.data`.

  Returns:
    Tuple of np.darray `x_train` with 178 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  path = os.path.expanduser(path)
  filename = 'wine.data'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/' \
          'wine/wine.data'
    maybe_download_and_extract(path, url)

  with open(os.path.join(path, filename)) as f:
    iterator = csv.reader(f)
    x_train = []
    for row in iterator:
      x_train.append(row)
  x_train = np.array(x_train, dtype=np.float)
  columns = ['alcohol',
             'malic acid',
             'ash',
             'alcalinity of ash',
             'magnesium',
             'total phenols',
             'flavanoids',
             'nonflavanoid phenols',
             'proanthocyanins',
             'color intensity',
             'hue',
             'OD280/OD315 of diluted wines',
             'proline']
  metadata = {'columns': columns}
  return x_train, metadata
