# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def spto87(path):
  """SP Return Data to October 1987

  The daily log returns on the S&P index value from Tuesday 5th January
  1960 until Friday 16 October 1987. The data are contained in a numeric
  vector. The dates of each observation are contained in a `times`
  attribute, which is an object of class `"POSIXct"` (see
  `DateTimeClasses`).

  A numeric vector containing 6985 observations, with a `times`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `spto87.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6985 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'spto87.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/evir/spto87.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='spto87.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
