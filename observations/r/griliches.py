# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def griliches(path):
  """Wage Datas

  a cross-section from 1980

  *number of observations* : 758

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  rns
      residency in the southern states (first observation) ?

  rns80
      same variable for 1980

  mrt
      married (first observation) ?

  mrt80
      same variable for 1980

  smsa
      residency in metropolitan areas (first observation) ?

  smsa80
      same variable for 1980

  med
      mother's education in years

  iq
      IQ score

  kww
      score on the “knowledge of the world of work” test

  year
      year of the observation

  age
      age (first observation)

  age80
      same variable for 1980

  school
      completed years of schooling (first observation)

  school80
      same variable for 1980

  expr
      experience in years (first observation)

  expr80
      same variable for 1980

  tenure
      tenure in years (first observation)

  tenure80
      same variable for 1980

  lw
      log wage (first observation)

  lw80
      same variable for 1980

  Blackburn, M. and Neumark D. (1992) “Unobserved ability, efficiency
  wages, and interindustry wage differentials”, *Quarterly Journal of
  Economics*, **107**, 1421-1436.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `griliches.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 758 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'griliches.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Griliches.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='griliches.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
