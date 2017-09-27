# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def icecream(path):
  """Ice Cream Consumption

  four–weekly observations from 1951–03–18 to 1953–07–11

  *number of observations* : 30

  *observation* : country

  *country* : United States

  A time serie containing :

  cons
      consumption of ice cream per head (in pints);

  income
      average family income per week (in US Dollars);

  price
      price of ice cream (per pint);

  temp
      average temperature (in Fahrenheit);

  Hildreth, C. and J. Lu (1960) *Demand relations with autocorrelated
  disturbances*, Technical Bulletin No 2765, Michigan State University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `icecream.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'icecream.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Icecream.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='icecream.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
