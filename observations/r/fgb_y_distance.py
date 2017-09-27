# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fgb_y_distance(path):
  """FGByDistance

  Field goal results in the NFL (by distance)

  A dataset with 51 observations on the following 7 variables.

  `Row`

  Case ID

  `Dist`

  Distance of the attempt (in yards)

  `N`

  Number of kicks attempted from that distance

  `Makes`

  Nmber of kicks made from that distance

  `PropMakes`

  Proportion of attempts made

  `Blocked`

  Number of kicks blocked

  `PropBlocked`

  Proportion of kicks blocked

  We thank Sean Forman and Doug Drinen of Sports Reference LLC for

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fgb_y_distance.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fgb_y_distance.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FGByDistance.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fgb_y_distance.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
