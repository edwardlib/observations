# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def males1(path):
  """Wages and Education of Young Males

  A panel of 545 observations from 1980 to 1987

  *total number of observations* : 4360

  *observation* : individuals

  *country* : United States

  A data frame containing :

  nr
      identifier

  year
      year

  school
      years of schooling

  exper
      years of experience (computed as `age-6-school`)

  union
      wage set by collective bargaining ?

  ethn
      a factor with levels `black, hisp, other`

  married
      married?

  health
      health problem ?

  wage
      log of hourly wage

  industry
      a factor with 12 levels

  occupation
      a factor with 9 levels

  residence
      a factor with levels
      `rural area, north east, northern central, south`

  Journal of Applied Econometrics data archive
  http://qed.econ.queensu.ca/jae/1998-v13.2/vella-verbeek/.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `males1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4360 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'males1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/Males.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='males1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
