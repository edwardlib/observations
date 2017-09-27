# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def blue_jays(path):
  """Blue Jays

  Body measurements for a sample of blue jays

  A dataset with 123 observations on the following 9 variables.

  `BirdID`

  ID tag for bird

  `KnownSex`

  Sex coded as `F` or `M`

  `BillDepth`

  Thickness of the bill measured at the nostril (in mm)

  `BillWidth`

  Width of the bill (in mm)

  `BillLength`

  Length of the bill (in mm)

  `Head`

  Distance from tip of bill to back of head (in mm)

  `Mass`

  Body mass (in grams)

  `Skull`

  Distance from base of bill to hack of skull (in mm)

  `Sex`

  Sex coded as 0=female or 1=male


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `blue_jays.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 123 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'blue_jays.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/BlueJays.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='blue_jays.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
