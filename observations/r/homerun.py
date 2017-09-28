# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def homerun(path):
  """Sample Data on Home Runs Hit By Mark McGwire and Sammy Sosa in 1998.

  Game-by-game information for the 1998 season for Mark McGwire and Sammy
  Sosa. Data are a subset of the dataset provided in Simonoff (1998).

  A data frame containing 5 variables ("gameno", "month", "homeruns",
  "playerstatus", "player") and 326 observations.

  `gameno`
      an integer variable denoting the game number

  `month`
      a factor variable taking with levels "March" through "September"
      denoting the month of the game

  `homeruns`
      an integer vector denoting the number of homeruns hit in that game
      for that player

  `playerstatus`
      an integer vector equal to "0" if the player played in the game, and
      "1" if they did not.

  `player`
      an integer vector equal to "0" (McGwire) or "1" (Sosa)

  https://ww2.amstat.org/publications/jse/v6n3/datasets.simonoff.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `homerun.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 314 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'homerun.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/homerun.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='homerun.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
