# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def markets(path):
  """Markets

  Daily changes in two stock market indices

  A dataset with 56 observations on the following 5 variables.

  `DJIAch`

  Change in Dow Jones Industrial Average

  `Date`

  Date: 06-Aug-09 to 02-Nov-09

  `Nik225ch`

  Change in Nikkei 225 stock average

  `Up`

  Indicator for positive Nikkei change

  `lagNik`

  Previous day's Nikkei change

  Dow Jones Industrial Average:
http://markets.cbsnews.com/cbsnews/quote/historical?Month=11&Symbol=310%3A998
  313&Year=2009&Range=12&tag=cbsnewsSectionsArea
  Historical Nikkei 225 index:

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `markets.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'markets.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Markets.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='markets.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
