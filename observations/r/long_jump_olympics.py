# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def long_jump_olympics(path):
  """LongJumpOlympics

  Winning distances in men's Olympic long jump competitions (1920-2008)

  A dataset with 26 observations on the following 2 variables.

  `Year`

  Year of the Olympics (1900-2008)

  `Gold`

  Winning men's long jump distance (in meters)

  Historcial Olympic long ump results at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `long_jump_olympics.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'long_jump_olympics.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/LongJumpOlympics.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='long_jump_olympics.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
