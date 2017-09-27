# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def budget_food(path):
  """Budget Share of Food for Spanish Households

  a cross-section from 1980

  *number of observations* : 23972

  *observation* : households

  *country* : Spain

  A dataframe containing :

  wfood
      percentage of total expenditure which the household has spent on
      food

  totexp
      total expenditure of the household

  age
      age of reference person in the household

  size
      size of the household

  town
      size of the town where the household is placed categorised into 5
      groups: 1 for small towns, 5 for big ones

  sex
      sex of reference person (man,woman)

  Delgado, A. and Juan Mora (1998) “Testing non–nested semiparametric
  models : an application to Engel curves specification”, *Journal of
  Applied Econometrics*, **13(2)**, 145–162.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `budget_food.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23972 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'budget_food.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/BudgetFood.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='budget_food.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
