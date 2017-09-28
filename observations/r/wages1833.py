# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wages1833(path):
  """Wages of Lancashire Cotton Factory Workers in 1833

  The `wages1833` data frame gives the wages of Lancashire cotton
  factory workers in 1833.

  This data frame contains the following columns:

  age
      age in years

  mnum
      number of male workers

  mwage
      average wage of male workers

  fnum
      number of female workers

  fwage
      average wage of female workers

  Boot, H.M. 1995. How Skilled Were the Lancashire Cotton Factory Workers
  in 1833? Economic History Review 48: 283-303.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wages1833.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wages1833.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/wages1833.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wages1833.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
