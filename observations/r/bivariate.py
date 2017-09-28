# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bivariate(path):
  """Sample data for bivariate probit regression

  Sample data for the bivariate probit regression.

  A table containing 6 variables ("y1", "y2", "x1", "x2", "x3", and "x4")
  and 78 observations.

  This is a cleaned and relabelled version of the sanction data set,
  available in Zelig.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bivariate.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 78 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bivariate.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/bivariate.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bivariate.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
