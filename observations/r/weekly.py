# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def weekly(path):
  """Weekly S&P Stock Market Data

  Weekly percentage returns for the S&P 500 stock index between 1990 and
  2010.

  A data frame with 1089 observations on the following 9 variables.

  `Year`
      The year that the observation was recorded

  `Lag1`
      Percentage return for previous week

  `Lag2`
      Percentage return for 2 weeks previous

  `Lag3`
      Percentage return for 3 weeks previous

  `Lag4`
      Percentage return for 4 weeks previous

  `Lag5`
      Percentage return for 5 weeks previous

  `Volume`
      Volume of shares traded (average number of daily shares traded in
      billions)

  `Today`
      Percentage return for this week

  `Direction`
      A factor with levels `Down` and `Up` indicating whether the
      market had a positive or negative return on a given week

  Raw values of the S&P 500 were obtained from Yahoo Finance and then
  converted to percentages and lagged.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `weekly.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1089 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'weekly.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Weekly.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='weekly.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
