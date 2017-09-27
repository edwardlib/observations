# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lake_huron(path):
  """Level of Lake Huron 1875–1972

  Annual measurements of the level, in feet, of Lake Huron 1875–1972.

  A time series of length 98.

  Brockwell, P. J. and Davis, R. A. (1991). *Time Series and Forecasting
  Methods*. Second edition. Springer, New York. Series A, page 555.

  Brockwell, P. J. and Davis, R. A. (1996). *Introduction to Time Series

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lake_huron.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 98 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lake_huron.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/LakeHuron.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lake_huron.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
