# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sp500(path):
  """Returns on Standard \\& Poor's 500 Index

  daily observations from 1981–01 to 1991–04

  *number of observations* : 2783

  A dataframe containing :

  r500
      daily return S\\&P500 (change in log index)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sp500.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2783 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sp500.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/SP500.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sp500.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
