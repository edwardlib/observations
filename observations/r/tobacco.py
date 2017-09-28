# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tobacco(path):
  """Households Tobacco Budget Share

  a cross-section from 1995-96

  *number of observations* : 2724

  *observation* : individuals

  *country* : Belgium

  A dataframe containing :

  occupation
      a factor with levels (bluecol,whitecol,inactself), the last level
      being inactive and self-employed

  region
      a factor with levels (flanders,wallon,brussels)

  nkids
      number of kids of more than two years old

  nkids2
      number of kids of less than two years old

  nadults
      number of adults in household

  lnx
      log of total expenditures

  stobacco
      budgetshare of tobacco

  salcohol
      budgetshare of alcohol

  age
      age in brackets (0-4)

  National Institute of Statistics (NIS), Belgium.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tobacco.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2724 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tobacco.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Tobacco.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tobacco.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
