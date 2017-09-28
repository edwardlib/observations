# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cigarette(path):
  """The Cigarette Consumption Panel Data Set

  a panel of 48 observations from 1985 to 1995

  *number of observations* : 528

  *observation* : regional

  *country* : United States

  A dataframe containing :

  state
      state

  year
      year

  cpi
      consumer price index

  pop
      state population

  packpc
      number of packs per capita

  income
      state personal income (total, nominal)

  tax
      average state, federal, and average local excise taxes for fiscal
      year

  avgprs
      average price during fiscal year, including sales taxes

  taxs
      average excise taxes for fiscal year, including sales taxes

  Professor Jonathan Gruber, MIT.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cigarette.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 528 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cigarette.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Cigarette.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cigarette.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
