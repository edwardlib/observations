# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nhtemp(path):
  """Average Yearly Temperatures in New Haven

  The mean annual temperature in degrees Fahrenheit in New Haven,
  Connecticut, from 1912 to 1971.

  A time series of 60 observations.

  Vaux, J. E. and Brinker, N. B. (1972) *Cycles*, **1972**, 117–121.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nhtemp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nhtemp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/nhtemp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nhtemp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
