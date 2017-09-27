# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def parity(path):
  """Purchasing Power Parity and other parity relationships

  A panel of 104 quarterly observations from 1973Q1 to 1998Q4

  *total number of observations* : 1768

  *observation* : country

  *country* : OECD

  A data frame containing :

  country
      country codes: a factor with 17 levels

  time
      the quarter index, 1973Q1-1998Q4

  ls
      log spot exchange rate vs. USD

  lp
      log price level

  is
      short term interest rate

  il
      long term interest rate

  ld
      log price differential vs. USA

  uis
      U.S. short term interest rate

  uil
      U.S. long term interest rate

  Coakley, J., Fuertes, A. M., and Smith, R. (2006) “Unobserved
  heterogeneity in panel time series models”, *Computational Statistics &
  Data Analysis*, **50**\ (9), 2361–2380.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `parity.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1768 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'parity.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/Parity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='parity.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
