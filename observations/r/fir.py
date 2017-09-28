# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fir(path):
  """Counts of Balsam-fir Seedlings

  The `fir` data frame has 50 rows and 3 columns.

  The number of balsam-fir seedlings in each quadrant of a grid of 50 five
  foot square quadrants were counted. The grid consisted of 5 rows of 10
  quadrants in each row.

  This data frame contains the following columns:

  `count`
      The number of seedlings in the quadrant.

  `row`
      The row number of the quadrant.

  `col`
      The quadrant number within the row.

  Davison, A.C. and Hinkley, D.V. (1997) *Bootstrap Methods and Their

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fir.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fir.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/fir.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fir.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
