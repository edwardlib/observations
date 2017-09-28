# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_pop(path):
  """Population of the United States

  The `USPop` data frame has 22 rows and 1 columns. This is a decennial
  time-series, from 1790 to 2000.

  This data frame contains the following columns:

  year
      census year.

  population
      Population in millions.

  U.S.~Census Bureau:
  http://www.census-charts.com/Population/pop-us-1790-2000.html,
  downloaded 1 May 2008.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_pop.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_pop.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/USPop.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_pop.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
