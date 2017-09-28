# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def seatshare(path):
  """Left Party Seat Share in 11 OECD Countries

  This data set contains time-series data of the seat shares in the lower
  legislative house of left leaning parties over time, as well as the
  level of unemployment. Data follows the style used in Hibbs (1977).

  A table containing N variables ("country","year","unemp","leftseat") and
  384 observations split across 11 countries.

  OECD data and Mackie and Rose (1991), extended to further years.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `seatshare.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 384 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'seatshare.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/seatshare.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='seatshare.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
