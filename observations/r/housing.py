# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def housing(path):
  """Sales Prices of Houses in the City of Windsor

  a cross-section from 1987

  *number of observations* : 546

  *observation* : goods

  *country* : Canada

  A dataframe containing :

  price
      sale price of a house

  lotsize
      the lot size of a property in square feet

  bedrooms
      number of bedrooms

  bathrms
      number of full bathrooms

  stories
      number of stories excluding basement

  driveway
      does the house has a driveway ?

  recroom
      does the house has a recreational room ?

  fullbase
      does the house has a full finished basement ?

  gashw
      does the house uses gas for hot water heating ?

  airco
      does the house has central air conditioning ?

  garagepl
      number of garage places

  prefarea
      is the house located in the preferred neighbourhood of the city ?

  Anglin, P.M. and R. Gencay (1996) “Semiparametric estimation of a
  hedonic price function”, *Journal of Applied Econometrics*, **11(6)**,
  633-648.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `housing.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 546 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'housing.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Housing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='housing.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
