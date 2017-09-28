# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def benefits(path):
  """Unemployment of Blue Collar Workers

  a cross-section from 1972

  *number of observations* : 4877

  *observation* : individuals

  *country* : United States

  A time serie containing :

  stateur
      state unemployment rate (in %)

  statemb
      state maximum benefit level

  state
      state of residence code

  age
      age in years

  tenure
      years of tenure in job lost

  joblost
      a factor with levels
      (slack\\\_work,position\\\_abolished,seasonal\\\_job\\\_ended,other)

  nwhite
      non-white ?

  school12
      more than 12 years of school ?

  sex
      a factor with levels (male,female)

  bluecol
      blue collar worker ?

  smsa
      lives is smsa ?

  married
      married ?

  dkids
      has kids ?

  dykids
      has young kids (0-5 yrs) ?

  yrdispl
      year of job displacement (1982=1,..., 1991=10)

  rr
      replacement rate

  head
      is head of household ?

  ui
      applied for (and received) UI benefits ?

  McCall, B.P. (1995) “The impact of unemployment insurance benefit levels
  on recipiency”, *Journal of Business and Economic Statistics*, **13**,
  189–198.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `benefits.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4877 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'benefits.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Benefits.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='benefits.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
