# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def n_f_l2007_standings(path):
  """NFL2007Standings

  Standings for National Football League teams in 2007

  A dataset with 32 observations on the following 10 variables.

  `Team`

  Team name

  `Conference`

  Conference: `AFC` or `NFC`

  `Division`

  Division within conference: `ACE`, `ACN`, `ACS`, `ACW`, `NCE`,
  `NCN`, `NCS`, `NCW`

  `Wins`

  Number of wins (out of 16 games)

  `Losses`

  Number of losses

  `WinPct`

  Proportion of games won (Wins/16)

  `PointsFor`

  Total points scored by the team

  `PointsAgainst`

  Total points scored against the team

  `NetPts`

  PointsFor minus PointsAgainst

  `TDs`

  Number of touchdowns scored by the team


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `n_f_l2007_standings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'n_f_l2007_standings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/NFL2007Standings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='n_f_l2007_standings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
