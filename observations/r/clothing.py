# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def clothing(path):
  """Sales Data of Men's Fashion Stores

  a cross-section from 1990

  *number of observations* : 400

  *observation* : production units

  *country* : Netherland

  A dataframe containing :

  tsales
      annual sales in Dutch guilders

  sales
      sales per square meter

  margin
      gross-profit-margin

  nown
      number of owners (managers)

  nfull
      number of full-timers

  npart
      number of part-timers

  naux
      number of helpers (temporary workers)

  hoursw
      total number of hours worked

  hourspw
      number of hours worked per worker

  inv1
      investment in shop-premises

  inv2
      investment in automation.

  ssize
      sales floorspace of the store (in m$^2$).

  start
      year start of business

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `clothing.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'clothing.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Clothing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='clothing.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
