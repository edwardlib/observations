# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def koch(path):
  """Ordinal Data from Koch

  The `koch` data frame has 288 rows and 4 columns.

  This data frame contains the following columns:

  trt
      a numeric vector

  day
      a numeric vector

  y
      an ordered factor with levels: `1` < `2` < `3`

  id
      a numeric vector

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `koch.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 288 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'koch.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/geepack/koch.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='koch.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
