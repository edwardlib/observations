# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def houses(path):
  """Houses

  Houses

  A dataset with 20 observations on the following 3 variables.

  `Price`

  Selling price (in dollars)

  `Size`

  Size of the house (in square feet)

  `Lot`

  Area of the house's lot (in square feet)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `houses.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'houses.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Houses.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='houses.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
