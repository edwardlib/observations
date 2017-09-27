# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def workinghours(path):
  """Wife Working Hours

  a cross-section from 1987

  *number of observations* : 3382

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  hours
      wife working hours per year

  income
      the other household income in hundreds of dollars

  age
      age of the wife

  education
      education years of the wife

  child5
      number of children for ages 0 to 5

  child13
      number of children for ages 6 to 13

  child17
      number of children for ages 14 to 17

  nonwhite
      non–white ?

  owned
      is the home owned by the household ?

  mortgage
      is the home on mortgage ?

  occupation
      occupation of the husband, one of mp (manager or

  unemp
      local unemployment rate in %

  Lee, Myoung–Jae (1995) “Semi–parametric estimation of simultaneous
  equations with limited dependent variables : a case study of female
  labour supply”, *Journal of Applied Econometrics*, **10(2)**,
  april–june, 187–200.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `workinghours.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3382 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'workinghours.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Workinghours.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='workinghours.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
