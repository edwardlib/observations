# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def siemens(path):
  """Daily Log Returns on Siemens Share Price

  These data are the daily log returns on Siemens share price from Tuesday
  2nd January 1973 until Tuesday 23rd July 1996. The data are contained in
  a numeric vector. The dates of each observation are contained in a
  `times` attribute, which is an object of class `"POSIXct"` (see
  `DateTimeClasses`). Note that these data form an irregular time series
  because no trading takes place at the weekend.

  A numeric vector containing 6146 observations, with a `times`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `siemens.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6146 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'siemens.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/evir/siemens.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='siemens.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
