# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kmenta2(path):
  """Simulation Data for model Three-Stage Least Square (threesls) that corresp
  onds to method 3SLS of systemfit

  Dataframe contains 20 annual observations of a supply/demand model with
  5 variables. Columns are q=Food consumption per capita, p=Ratio of food
  price to general consumer prices, d=Disposable income in contstant
  dollars, f=Ratio of preceding year's prices received by farmers to
  general consumer prices, a=Time index.

  A table containing 5 variables ("q", "p", "d", "f","a") and 20

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kmenta2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kmenta2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/kmenta.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kmenta2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
