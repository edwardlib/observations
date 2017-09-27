# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def trucks(path):
  """Truck Accidents Data

  Data from a study in England in two periods from November 1969 to
  October 1971 and November 1971 to October 1973. A new compulsory safety
  measure for trucks was introduced in October 1971. Therefore, the
  question is whether the safety measure had an effect on the number of
  accidents and on the point of collision on the truck.

  A data frame with 24 observations on 5 variables.

  Freq
      frequency of accidents involving trucks.

  period
      factor indicating time period (before, after) 1971-11-01.

  collision
      factor indicating whether the collision was in the back or forward
      (including the front and the sides) of the truck (back, forward).

  parked
      factor indicating whether the truck was parked (yes, no).

  light
      factor indicating light conditions: day light (daylight), night on
      an illuminated road (night, illuminate), night on a dark road
      (night, dark).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  Table 6.8.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `trucks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'trucks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Trucks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='trucks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
