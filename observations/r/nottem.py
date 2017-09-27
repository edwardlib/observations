# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nottem(path):
  """Average Monthly Temperatures at Nottingham, 1920–1939

  A time series object containing average air temperatures at Nottingham
  Castle in degrees Fahrenheit for 20 years.

  Anderson, O. D. (1976) *Time Series Analysis and Forecasting: The
  Box-Jenkins approach.* Butterworths. Series R.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nottem.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 240 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nottem.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/nottem.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nottem.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
