# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def speed(path):
  """Speed

  Highway fatality rates 1987-2007

  A dataset with 21 observations on the following 3 variables.

  `Year`

  Year (1987-2007

  `FatalityRate`

  Number of fatalites on interstate highways (per 100 million
  vehicle-miles)

  `StateControl`

  `0`\ =1987-1994 or `1`\ =1995-2007

  Data from the National Highway Saftey Administration website at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `speed.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'speed.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Speed.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='speed.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
