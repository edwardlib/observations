# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def siegels_ex(path):
  """Siegel's Exact Fit Example Data

  A small counterexample data set devised by Andrew Siegel. Six (out of
  nine) data points lie on the line *y = 0* such that some robust
  regression estimators exhibit the “\ *exact fit*\ ” property.

  A data frame with 9 observations on the following 2 variables.

  `x`
      a numeric vector

  `y`
      a numeric vector

  Emerson and Hoaglin (1983, p.139)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `siegels_ex.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'siegels_ex.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/SiegelsEx.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='siegels_ex.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
