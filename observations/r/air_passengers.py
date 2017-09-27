# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def air_passengers(path):
  """Monthly Airline Passenger Numbers 1949-1960

  The classic Box & Jenkins airline data. Monthly totals of international
  airline passengers, 1949 to 1960.

  A monthly time series, in thousands.

  Box, G. E. P., Jenkins, G. M. and Reinsel, G. C. (1976) *Time Series
  Analysis, Forecasting and Control.* Third Edition. Holden-Day. Series G.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `air_passengers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 144 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'air_passengers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/AirPassengers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='air_passengers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
