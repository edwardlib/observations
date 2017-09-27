# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def attenu(path):
  """The Joyner–Boore Attenuation Data

  This data gives peak accelerations measured at various observation
  stations for 23 earthquakes in California. The data have been used by
  various workers to estimate the attenuating affect of distance on ground
  acceleration.

  A data frame with 182 observations on 5 variables.

  +--------+-----------+-----------+------------------------------------+
  | [,1]   | event     | numeric   | Event Number                       |
  +--------+-----------+-----------+------------------------------------+
  | [,2]   | mag       | numeric   | Moment Magnitude                   |
  +--------+-----------+-----------+------------------------------------+
  | [,3]   | station   | factor    | Station Number                     |
  +--------+-----------+-----------+------------------------------------+
  | [,4]   | dist      | numeric   | Station-hypocenter distance (km)   |
  +--------+-----------+-----------+------------------------------------+
  | [,5]   | accel     | numeric   | Peak acceleration (g)              |
  +--------+-----------+-----------+------------------------------------+

  Joyner, W.B., D.M. Boore and R.D. Porcella (1981). Peak horizontal
  acceleration and velocity from strong-motion records including records
  from the 1979 Imperial Valley, California earthquake. USGS Open File
  report 81-365. Menlo Park, Ca.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `attenu.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 182 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'attenu.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/attenu.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='attenu.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
