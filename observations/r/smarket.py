# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def smarket(path):
  """S&P Stock Market Data

  Daily percentage returns for the S&P 500 stock index between 2001 and
  2005.

  A data frame with 1250 observations on the following 9 variables.

  `Year`
      The year that the observation was recorded

  `Lag1`
      Percentage return for previous day

  `Lag2`
      Percentage return for 2 days previous

  `Lag3`
      Percentage return for 3 days previous

  `Lag4`
      Percentage return for 4 days previous

  `Lag5`
      Percentage return for 5 days previous

  `Volume`
      Volume of shares traded (number of daily shares traded in billions)

  `Today`
      Percentage return for today

  `Direction`
      A factor with levels `Down` and `Up` indicating whether the
      market had a positive or negative return on a given day

  Raw values of the S&P 500 were obtained from Yahoo Finance and then
  converted to percentages and lagged.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `smarket.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1250 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'smarket.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Smarket.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='smarket.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
