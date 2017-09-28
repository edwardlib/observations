# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hills(path):
  """Scottish Hill Races Data

  The record times in 1984 for 35 Scottish hill races.

  This data frame contains the following columns:

  dist
      distance, in miles (on the map)

  climb
      total height gained during the route, in feet

  time
      record time in hours

  A.C. Atkinson (1986) Comment: Aspects of diagnostic regression analysis.
  Statistical Science 1, 397-402.

  Also, in MASS library, with time in minutes.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hills.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 35 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hills.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/hills.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hills.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
