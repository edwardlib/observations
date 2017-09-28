# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wages1(path):
  """Wages, Experience and Schooling

  a panel of 595 observations from 1976 to 1982

  *number of observations* : 3294

  *observation* : individuals

  *country* : United States

  A time serie containing :

  exper
      experience in years

  sex
      a factor with levels (male,female)

  school
      years of schooling

  wage
      wage (in 1980 \\$) per hour

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wages1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3294 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wages1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Wages1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wages1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
