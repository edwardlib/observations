# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def auto_pollution(path):
  """AutoPollution

  AutoPollution

  A dataset with 36 observations on the following 4 variables.

  `Noise`

  Noise level (decibels)

  `Size`

  Vehicle size: `1`\ =small, `2`\ =medium, or `3`\ =large

  `Type`

  `1`\ =standard filer or `2`\ =new filter

  `Side`

  Side of vehicle: code1=right or `2`\ =left

  Data explanation and link can be found at
  http://lib.stat.cmu.edu/DASL/Stories/airpollutionfilters.html.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `auto_pollution.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'auto_pollution.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/AutoPollution.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='auto_pollution.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
