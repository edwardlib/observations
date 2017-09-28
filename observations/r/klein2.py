# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def klein2(path):
  """Simulation Data for model Two-Stage Least Square (twosls) that corresponds
   to method 2SLS of systemfit

  Dataframe contains annual observations of US economy from 1920 to 1940.
  The columns are, Year, C=Consumption, P=Corporate profits, P1=Previous
  year corporate profit,Wtot=Total wage, Wp=Private wage bill,
  Wg=Government wage bill,I=Investment, K1=Previous year capital
  stock,X=GNP,G=Government spending, T=Taxes, X1=Previous year GNP,
  Tm=Year-1931.

  A table containing 14 variables ("year", "C", "P", "P1","Wtot", "Wp",
  "Wg", "I", "K1","X", "G", "T", "X1", "Tm") and 21 observations.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `klein2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'klein2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/klein.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='klein2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
