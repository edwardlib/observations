# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def airmiles(path):
  """Passenger Miles on Commercial US Airlines, 1937–1960

  The revenue passenger miles flown by commercial airlines in the United
  States for each year from 1937 to 1960.

  A time series of 24 observations; yearly, 1937–1960.

  F.A.A. Statistical Handbook of Aviation.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `airmiles.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'airmiles.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/airmiles.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='airmiles.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
