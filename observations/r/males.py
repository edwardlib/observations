# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def males(path):
  """Wages and Education of Young Males

  a panel of 545 observations from 1980 to 1987

  *number of observations* : 4360

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  nr
      identifier

  year
      year

  school
      years of schooling

  exper
      years of experience (=age-6-school)

  union
      wage set by collective bargaining ?

  ethn
      a factor with levels (black,hisp,other)

  maried
      maried ?

  health
      health problem ?

  wage
      log of hourly wage

  industry
      a factor with 12 levels

  occupation
      a factor with 9 levels

  residence
      a factor with levels (rural area, north east, nothern central,
      south)

  National Longitudinal Survey (NLS Youth Sample).

  Vella, F. and M. Verbeek (1998) “Whose wages do unions raise ? A dynamic
  model of unionism and wage”, *Journal of Applied Econometrics*, **13**,
  163–183.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `males.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4360 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'males.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Males.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='males.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
