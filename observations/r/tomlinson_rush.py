# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tomlinson_rush(path):
  """LaDainian Tomlinson Rushing Yards

  Rushing yards for each game LaDainian Tomlinson played in the 2006
  National Football League (NFL regular) season.

  A dataset with 16 observations on the following 4 variables.

  `Game`

  Week number in the 2006 season

  `Opponent`

  Name of opposing team

  `Attempts`

  Number of rushing attempts

  `Yards`

  Total yards gamed rushing for the game

  Data downloaded from

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tomlinson_rush.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tomlinson_rush.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/TomlinsonRush.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tomlinson_rush.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
