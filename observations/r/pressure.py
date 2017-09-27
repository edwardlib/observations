# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pressure(path):
  """Vapor Pressure of Mercury as a Function of Temperature

  Data on the relation between temperature in degrees Celsius and vapor
  pressure of mercury in millimeters (of mercury).

  A data frame with 19 observations on 2 variables.

  +---------+---------------+-----------+-----------------------+
  | [, 1]   | temperature   | numeric   | temperature (deg C)   |
  +---------+---------------+-----------+-----------------------+
  | [, 2]   | pressure      | numeric   | pressure (mm)         |
  +---------+---------------+-----------+-----------------------+

  Weast, R. C., ed. (1973) *Handbook of Chemistry and Physics*. CRC Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pressure.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 19 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pressure.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/pressure.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pressure.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
