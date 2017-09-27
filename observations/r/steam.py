# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def steam(path):
  """The Saturated Steam Pressure Data

  Temperature and pressure in a saturated steam driven experimental
  device.

  The data frame contains the following components:

  `Temp`
      temperature, in degrees Celsius.

  `Press`
      pressure, in Pascals.

  N.R. Draper and H. Smith (1981) *Applied Regression Analysis.* Wiley,
  pp. 518–9.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `steam.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'steam.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/steam.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='steam.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
