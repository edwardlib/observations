# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def barro(path):
  """Barro Data

  Version of the Barro Growth Data used in Koenker and Machado(1999). This
  is a regression data set consisting of 161 observations on determinants
  of cross country GDP growth rates. There are 13 covariates with dimnames
  corresponding to the original Barro and Lee source. See
  http://www.nber.org/pub/barro.lee/. The first 71 observations are on the
  period 1965-75, remainder on 1987-85.

  A data frame containing 161 observations on 14 variables:

  +---------+----------------------------------+
  | [,1]    | "Annual Change Per Capita GDP"   |
  +---------+----------------------------------+
  | [,2]    | "Initial Per Capita GDP"         |
  +---------+----------------------------------+
  | [,3]    | "Male Secondary Education"       |
  +---------+----------------------------------+
  | [,4]    | "Female Secondary Education"     |
  +---------+----------------------------------+
  | [,5]    | "Female Higher Education"        |
  +---------+----------------------------------+
  | [,6]    | "Male Higher Education"          |
  +---------+----------------------------------+
  | [,7]    | "Life Expectancy"                |
  +---------+----------------------------------+
  | [,8]    | "Human Capital"                  |
  +---------+----------------------------------+
  | [,9]    | "Education/GDP"                  |
  +---------+----------------------------------+
  | [,10]   | "Investment/GDP"                 |
  +---------+----------------------------------+
  | [,11]   | "Public Consumption/GDP"         |
  +---------+----------------------------------+
  | [,12]   | "Black Market Premium"           |
  +---------+----------------------------------+
  | [,13]   | "Political Instability"          |
  +---------+----------------------------------+
  | [,14]   | "Growth Rate Terms Trade"        |
  +---------+----------------------------------+

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `barro.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 161 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'barro.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/quantreg/barro.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='barro.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
