# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gasoline(path):
  """Gasoline Consumption

  a panel of 18 observations from 1960 to 1978

  *number of observations* : 342

  *observation* : country

  *country* : OECD

  A dataframe containing :

  country
      a factor with 18 levels

  year
      the year

  lgaspcar
      logarithm of motor gasoline consumption per auto

  lincomep
      logarithm of real per-capita income

  lrpmg
      logarithm of real motor gasoline price

  lcarpcap
      logarithm of the stock of cars per capita

  Baltagi, B.H. and Y.J. Griggin (1983) “Gasoline demand in the OECD: an
  application of pooling and testing procedures”, *European Economic
  Review*, **22**.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gasoline.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 342 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gasoline.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Gasoline.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gasoline.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
