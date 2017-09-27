# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mun_exp(path):
  """Municipal Expenditure Data

  a panel of 265 observations from 1979 to 1987

  *number of observations* : 2385

  *observation* : regional

  *country* : Sweden

  A dataframe containing :

  id
      identification

  year
      date

  expend
      expenditure

  revenue
      revenue from taxes and fees

  grants
      grants from Central Government

  Dahlberg, M. and E. Johansson (2000) “An examination of the dynamic
  behavior of local government using GMM boot-strapping methods”, *Journal
  of Applied Econometrics*, **21**, 333-355.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mun_exp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2385 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mun_exp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/MunExp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mun_exp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
