from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def precip(path):
  """Annual Precipitation in US Cities

  The average amount of precipitation (rainfall) in inches for each of 70
  United States (and Puerto Rico) cities.

  A named vector of length 70.

  Statistical Abstracts of the United States, 1975.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `precip.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 70 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'precip.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/datasets/precip.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='precip.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
