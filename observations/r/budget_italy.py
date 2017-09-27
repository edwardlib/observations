# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def budget_italy(path):
  """Budget Shares for Italian Households

  a cross-section from 1973 to 1992

  *number of observations* : 1729

  *observation* : households

  *country* : Italy

  A dataframe containing :

  wfood
      food share

  whouse
      housing and fuels share

  wmisc
      miscellaneous share

  pfood
      food price

  phouse
      housing and fuels price

  pmisc
      miscellaneous price

  totexp
      total expenditure

  year
      year

  income
      income

  size
      household size

  pct
      cellule weight

  Bollino, Carlo Andrea, Frederico Perali and Nicola Rossi (2000) “Linear
  household technologies”, *Journal of Applied Econometrics*, **15(3)**,
  253–274.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `budget_italy.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1729 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'budget_italy.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/BudgetItaly.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='budget_italy.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
