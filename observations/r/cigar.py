# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cigar(path):
  """Cigarette Consumption

  a panel of 46 observations from 1963 to 1992

  *number of observations* : 1380

  *observation* : regional

  *country* : United States

  A dataframe containing :

  state
      state abbreviation

  year
      the year

  price
      price per pack of cigarettes

  pop
      population

  pop16
      population above the age of 16

  cpi
      consumer price index (1983=100)

  ndi
      per capita disposable income

  sales
      cigarette sales in packs per capita

  pimin
      minimum price in adjoining states per pack of cigarettes

  Baltagi, B.H. and D. Levin (1992) “Cigarette taxation: raising revenues
  and reducing consumption”, *Structural Changes and Economic Dynamics*,
  **3**, 321–335.

  Baltagi, B.H., J.M. Griffin and W. Xiong (2000) “To pool or not to pool:
  homogeneous versus heterogeneous estimators applied to cigarette
  demand”, *Review of Economics and Statistics*, **82**, 117–126.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cigar.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1380 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cigar.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Cigar.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cigar.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
