# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def freeny(path):
  """Freeny's Revenue Data

  Freeny's data on quarterly revenue and explanatory variables.

  There are three ‘freeny’ data sets.

  `freeny.y` is a time series with 39 observations on quarterly revenue
  from (1962,2Q) to (1971,4Q).

  `freeny.x` is a matrix of explanatory variables. The columns are
  `freeny.y` lagged 1 quarter, price index, income level, and market
  potential.

  Finally, `freeny` is a data frame with variables `y`,
  `lag.quarterly.revenue`, `price.index`, `income.level`, and
  `market.potential` obtained from the above two data objects.

  A. E. Freeny (1977) *A Portable Linear Regression Package with Test
  Programs*. Bell Laboratories memorandum.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `freeny.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 39 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'freeny.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/freeny.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='freeny.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
