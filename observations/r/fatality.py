# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fatality(path):
  """Drunk Driving Laws and Traffic Deaths

  a panel of 48 observations from 1982 to 1988

  *number of observations* : 336

  *observation* : regional

  *country* : United States

  A dataframe containing :

  state
      state ID code

  year
      year

  mrall
      traffic fatality rate (deaths per 10000)

  beertax
      tax on case of beer

  mlda
      minimum legal drinking age

  jaild
      mandatory jail sentence ?

  comserd
      mandatory community service ?

  vmiles
      average miles per driver

  unrate
      unemployment rate

  perinc
      per capita personal income

  Pr. Christopher J. Ruhm, Department of Economics, University of North
  Carolina.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fatality.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 336 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fatality.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Fatality.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fatality.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
