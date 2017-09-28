# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def transact(path):
  """Transaction data

  Data on transaction times in branch offices of a large Australian bank.

  This data frame contains the following columns:

  t1
      number of type 1 transactions

  t2
      number of type 2 transactions

  time
      total transaction time, minutes

  Cunningham, R. and Heathcote, C. (1989), Estimating a non-Gaussian
  regression model with multicollinearity. Australian Journal of
  Statistics, 31,12-17.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `transact.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 261 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'transact.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Transact.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='transact.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
