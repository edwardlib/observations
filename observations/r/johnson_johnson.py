# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def johnson_johnson(path):
  """Quarterly Earnings per Johnson & Johnson Share

  Quarterly earnings (dollars) per Johnson & Johnson share 1960–80.

  A quarterly time series

  Shumway, R. H. and Stoffer, D. S. (2000) *Time Series Analysis and its
  Applications*. Second Edition. Springer. Example 1.1.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `johnson_johnson.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 84 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'johnson_johnson.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/JohnsonJohnson.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='johnson_johnson.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
