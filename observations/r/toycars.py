# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def toycars(path):
  """Toy Cars Data

  The `toycars` data frame has 27 rows and 3 columns. Observations are
  on the distance traveled by one of three different toy cars on a smooth
  surface, starting from rest at the top of a 16 inch long ramp tilted at
  varying angles.

  This data frame contains the following columns:

  angle
      tilt of ramp, in degrees

  distance
      distance traveled, in meters

  car
      a numeric code (1 = first car, 2 = second car, 3 = third car)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `toycars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'toycars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/toycars.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='toycars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
