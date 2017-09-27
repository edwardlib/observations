# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def airq(path):
  """Air Quality for Californian Metropolitan Areas

  a cross-section from 1972

  *number of observations* : 30

  *observation* : regional

  *country* : United States

  A dataframe containing :

  airq
      indicator of air quality (the lower the better)

  vala
      value added of companies (in thousands of dollars)

  rain
      amount of rain (in inches)

  coas
      is it a coastal area ?

  dens
      population density (per square mile)

  medi
      average income per head (in US dollars)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `airq.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'airq.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Airq.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='airq.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
