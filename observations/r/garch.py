# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def garch(path):
  """Daily Observations on Exchange Rates of the US Dollar Against Other Curren
  cies

  daily observations from 1980–01 to 1987–05–21

  *number of observations* : 1867

  *observation* : country

  *country* : World

  A dataframe containing :

  date
      date of observation (yymmdd)

  day
      day of the week (a factor)

  dm
      exchange rate Dollar/Deutsch Mark

  ddm
      dm-dm(-1)

  bp
      exchange rate of Dollar/British Pound

  cd
      exchange rate of Dollar/Canadian Dollar

  dy
      exchange rate of Dollar/Yen

  sf
      exchange rate of Dollar/Swiss Franc

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `garch.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1867 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'garch.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Garch.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='garch.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
