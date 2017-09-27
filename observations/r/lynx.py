# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lynx(path):
  """Annual Canadian Lynx trappings 1821–1934

  Annual numbers of lynx trappings for 1821–1934 in Canada. Taken from
  Brockwell & Davis (1991), this appears to be the series considered by
  Campbell & Walker (1977).

  Brockwell, P. J. and Davis, R. A. (1991) *Time Series and Forecasting
  Methods.* Second edition. Springer. Series G (page 557).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lynx.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 114 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lynx.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/lynx.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lynx.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
