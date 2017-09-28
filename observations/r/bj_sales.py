# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bj_sales(path):
  """Sales Data with Leading Indicator

  The sales time series `BJsales` and leading indicator `BJsales.lead`
  each contain 150 observations. The objects are of class `"ts"`.

  The data are given in Box & Jenkins (1976). Obtained from the Time
  Series Data Library at
  http://www-personal.buseco.monash.edu.au/~hyndman/TSDL/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bj_sales.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 150 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bj_sales.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/BJsales.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bj_sales.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
