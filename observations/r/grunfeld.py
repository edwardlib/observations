# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grunfeld(path):
  """Grunfeld Investment Data

  a panel of 10 observations from 1935 to 1954

  *number of observations* : 200

  *observation* : production units

  *country* : United States

  A dataframe containing :

  firm
      observation

  year
      date

  inv
      gross Investment

  value
      value of the firm

  capital
      stock of plant and equipment

  Moody's Industrial Manual, Survey of Current Business.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grunfeld.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 200 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grunfeld.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Grunfeld.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grunfeld.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
