# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leaftemp_all(path):
  """Full Leaf and Air Temperature Data Set

  The `leaftemp.all` data frame has 62 rows and 9 columns.

  This data frame contains the following columns:

  glasshouse
      a factor with levels `A`, `B`, `C`

  CO2level
      a factor with Carbon Dioxide Levels: `high`, `low`, `medium`

  day
      a factor

  light
      a numeric vector

  CO2
      a numeric vector

  tempDiff
      Difference between Leaf and Air Temperature

  BtempDiff
      a numeric vector

  airTemp
      Air Temperature

  vapPress
      Vapour Pressure


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leaftemp_all.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leaftemp_all.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/leaftemp.all.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leaftemp_all.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
