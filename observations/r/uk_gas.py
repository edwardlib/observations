# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def uk_gas(path):
  """UK Quarterly Gas Consumption

  Quarterly UK gas consumption from 1960Q1 to 1986Q4, in millions of
  therms.

  A quarterly time series of length 108.

  Durbin, J. and Koopman, S. J. (2001) *Time Series Analysis by State
  Space Methods.* Oxford University Press. http://www.ssfpack.com/dkbook/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `uk_gas.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 108 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'uk_gas.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/UKgas.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='uk_gas.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
