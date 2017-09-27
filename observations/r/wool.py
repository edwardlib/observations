# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wool(path):
  """Australian Relative Wool Prices

  `wool` is a time series of class `"ts"` and contains 309
  observations.

  Each week that the market is open the Australian Wool Corporation set a
  floor price which determines their policy on intervention and is
  therefore a reflection of the overall price of wool for the week in
  question. Actual prices paid can vary considerably about the floor
  price. The series here is the log of the ratio between the price for
  fine grade wool and the floor price, each market week between July 1976
  and Jun 1984.

  The data were obtained from

  Diggle, P.J. (1990) *Time Series: A Biostatistical Introduction*. Oxford
  University Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wool.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 309 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wool.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/wool.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wool.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
