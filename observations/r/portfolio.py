from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def portfolio(path):
  """Portfolio Data

  A simple simulated data set containing 100 returns for each of two
  assets, X and Y. The data is used to estimate the optimal fraction to
  invest in each asset to minimize investment risk of the combined
  portfolio. One can then use the Bootstrap to estimate the standard error
  of this estimate.

  A data frame with 100 observations on the following 2 variables.

  `X`
      Returns for Asset X

  `Y`
      Returns for Asset Y

  Simulated data

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `portfolio.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'portfolio.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/ISLR/Portfolio.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='portfolio.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
