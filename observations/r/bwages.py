# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bwages(path):
  """Wages in Belgium

  a cross-section from 1994

  *number of observations* : 1472

  *observation* : individuals

  *country* : Belgium

  A dataframe containing :

  wage
      gross hourly wage rate in euro

  educ
      education level from 1 [low] to 5 [high]

  exper
      years of experience

  sex
      a factor with levels (males,female)

  European Community Household Panel.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bwages.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1472 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bwages.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Bwages.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bwages.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
