# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def drivers(path):
  """Deaths of Car Drivers in Great Britain 1969-84

  A regular time series giving the monthly totals of car drivers in Great
  Britain killed or seriously injured Jan 1969 to Dec 1984. Compulsory
  wearing of seat belts was introduced on 31 Jan 1983

  Harvey, A.C. (1989) *Forecasting, Structural Time Series Models and the
  Kalman Filter.* Cambridge University Press, pp. 519–523.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `drivers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 192 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'drivers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/drivers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='drivers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
