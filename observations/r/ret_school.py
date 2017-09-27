# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ret_school(path):
  """Return to Schooling

  a panel of 48 observations from 1970 to 1986

  *number of observations* : 5225

  *observation* : individuals

  *country* : United States

  A time serie containing :

  wage76
      wage in 1876

  grade76
      grade level in 1976

  exp76
      experience 1n 1976

  black
      black ?

  south76
      lived in south in 1976 ?

  smsa76
      lived in smsa in 1976 ?

  region
      region, a factor with levels (un,midatl,enc,wnc,sa,esc,wsc,m,p)

  smsa66
      lived in smsa in 1966 ?

  momdad14
      lived with both parents at age 14 ?

  sinmom14
      lived with mother only at age 14 ?

  nodaded
      father has no formal education ?

  nomomed
      mother has no formal education ?

  daded
      mean grade level of father

  momed
      mean grade level of mother

  famed
      father's and mother's education, a factor with 9 levels

  age76
      age in 1976

  col4
      is any 4-year college nearby ?

  Kling, Jeffrey R. (2001) “Interpreting Instrumental Variables Estimates
  of the Return to Schooling”, *Journal of Business and Economic
  Statistics*, **19(3)**, july, 358–364.

  Dehejia, R.H. and S. Wahba (2002) “Propensity-score Matching Methods for
  Nonexperimental Causal Studies”, *Restat*, 151–161.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ret_school.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5225 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ret_school.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/RetSchool.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ret_school.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
