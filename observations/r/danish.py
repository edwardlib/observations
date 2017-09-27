# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def danish(path):
  """Danish Fire Insurance Claims

  These data describe large fire insurance claims in Denmark from Thursday
  3rd January 1980 until Monday 31st December 1990. The data are contained
  in a numeric vector. The dates of each observation are contained in a
  `times` attribute, which is an object of class `"POSIXct"` (see
  `DateTimeClasses`). They were supplied by Mette Rytgaard of Copenhagen
  Re. Note that these data form an irregular time series.

  A numeric vector containing 2167 observations, with a `times`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `danish.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2167 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'danish.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/evir/danish.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='danish.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
