# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wages(path):
  """Panel Datas of Individual Wages

  a panel of 595 observations from 1976 to 1982

  *number of observations* : 4165

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  exp
      years of full-time work experience

  wks
      weeks worked

  bluecol
      blue collar ?

  ind
      works in a manufacturing industry ?

  south
      resides in the south ?

  smsa
      resides in a standard metropolitan statistical are ?

  married
      married ?

  sex
      a factor with levels (male,female)

  union
      individual's wage set by a union contract ?

  ed
      years of education

  black
      is the individual black ?

  lwage
      logarithm of wage

  Cornwell, C. and P. Rupert (1988) “Efficient estimation with panel data:
  an empirical comparison of instrumental variables estimators”, *Journal
  of Applied Econometrics*, **3**, 149–155.

  Panel study of income dynamics.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wages.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4165 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wages.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Wages.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wages.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
