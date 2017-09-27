# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def baseball_times(path):
  """BaseballTimes

  Game times and boxscore information for baseball games

  A dataset with 15 observations on the following 7 variables.

  `Game`

  Code for opposing teams

  `League`

  `AL`\ = American League or `NL`\ =Mational League

  `Runs`

  Total number of runs scored (both teams)

  `Margin`

  Margin of victory (Winner-Loser score)

  `Pitchers`

  Total number of pitchers used (both teams

  `Attendance`

  Number of spectators at the game

  `Time`

  Total time for the game (in minutes)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `baseball_times.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'baseball_times.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/BaseballTimes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='baseball_times.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
