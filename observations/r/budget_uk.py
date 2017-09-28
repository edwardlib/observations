# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def budget_uk(path):
  """Budget Shares of British Households

  a cross-section from 1980 to 1982

  *number of observations* : 1519

  *observation* : households

  *country* : United Kingdown

  A dataframe containing :

  wfood
      budget share for food expenditure

  wfuel
      budget share for fuel expenditure

  wcloth
      budget share for clothing expenditure

  walc
      budget share for alcohol expenditure

  wtrans
      budget share for transport expenditure

  wother
      budget share for other good expenditure

  totexp
      total household expenditure (rounded to the nearest 10 UK pounds
      sterling)

  income
      total net household income (rounded to the nearest 10 UK pounds
      sterling)

  age
      age of household head

  children
      number of children

  Blundell, Richard, Alan Duncan and Krishna Pendakur (1998)
  “Semiparametric estimation and consumer demand”, *Journal of Applied
  Econometrics*, **13(5)**, 435–462.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `budget_uk.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1519 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'budget_uk.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/BudgetUK.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='budget_uk.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
