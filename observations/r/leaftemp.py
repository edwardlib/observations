# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leaftemp(path):
  """Leaf and Air Temperature Data

  These data consist of measurements of vapour pressure and of the
  difference between leaf and air temperature.

  This data frame contains the following columns:

  CO2level
      Carbon Dioxide level `low`, `medium`, `high`

  vapPress
      Vapour pressure

  tempDiff
      Difference between leaf and air temperature

  BtempDiff
      a numeric vector

  Katharina Siebke and Susan von Cammerer, Australian National University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leaftemp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leaftemp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/leaftemp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leaftemp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
