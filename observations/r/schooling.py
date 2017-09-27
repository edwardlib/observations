# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def schooling(path):
  """Wages and Schooling

  a cross-section from 1976

  *number of observations* : 3010

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  smsa66
      lived in smsa in 1966 ?

  smsa76
      lived in smsa in 1976 ?

  nearc2
      grew up near 2-yr college ?

  nearc4
      grew up near 4-yr college ?

  nearc4a
      grew up near 4-year public college ?

  nearc4b
      grew up near 4-year private college ?

  ed76
      education in 1976

  ed66
      education in 1966

  age76
      age in 1976

  daded
      dads education (imputed avg if missing)

  nodaded
      dads education imputed ?

  momed
      mothers education

  nomomed
      moms education imputed ?

  momdad14
      lived with mom and dad at age 14 ?

  sinmom14
      single mom at age 14 ?

  step14
      step parent at age 14 ?

  south66
      lived in south in 1966 ?

  south76
      lived in south in 1976 ?

  lwage76
      log wage in 1976 (outliers trimmed)

  famed
      mom-dad education class (1-9)

  black
      black ?

  wage76
      wage in 1976 (raw, cents per hour)

  enroll76
      enrolled in 1976 ?

  kww
      the kww score

  iqscore
      a normed IQ score

  mar76
      married in 1976 ?

  libcrd14
      library card in home at age 14 ?

  exp76
      experience in 1976

  National Longitudinal Survey of Young Men (NLSYM) .

  Card, D. (1995) *Using geographical variation in college proximity to
  estimate the return to schooling* *in* Christofides, L.N., E.K. Grant
  and R. Swidinsky (1995) *Aspects of labour market behaviour : essays in
  honour of John Vanderkamp*, University of Toronto Press, Toronto .

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `schooling.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3010 rows and 28 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'schooling.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Schooling.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='schooling.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
