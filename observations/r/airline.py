# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def airline(path):
  """Cost for U.S. Airlines

  a panel of 6 observations from 1970 to 1984

  *number of observations* : 90

  *observation* : production units

  *country* : United States

  A dataframe containing :

  airline
      airline

  year
      year

  cost
      total cost, in \\$1,000

  output
      output, in revenue passenger miles, index number

  pf
      fuel price

  lf
      load factor, the average capacity utilization of the fleet

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `airline.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'airline.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Airline.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='airline.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
