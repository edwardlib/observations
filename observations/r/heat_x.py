# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def heat_x(path):
  """Data from a heat exchanger laboratory

  These data were collected by engineering students at Calvin College. The
  apparatus consists of concentric pipes insulated from the environment so
  that as nearly as can be managed the only heat exchange is between the
  hot and cold water.

  A data frame with 6 observations on the following variables.

  -  `trial` trial number

  -  `T.cold.in` temperature (C) of the cold water as it enters the
     apparatus

  -  `T.cold.out` temperature (C) of the cold water as it leaves the
     apparatus

  -  `m.cold` flow rate (L/min) of the cold water

  -  `T.hot.in` temperature (C) of the hot water as it enters the
     apparatus

  -  `T.hot.out` temperature (C) of the hot water as it leaves the
     apparatus

  -  `m.hot` flow rate (L/min) of the hot water

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `heat_x.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'heat_x.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/HeatX.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='heat_x.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
