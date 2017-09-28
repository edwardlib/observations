# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bundesliga(path):
  """Ergebnisse der Fussball-Bundesliga

  Results from the first German soccer league (1963-2008).

  A data frame with 14018 observations and 7 variables.

  HomeTeam
      factor. Name of the home team.

  AwayTeam
      factor. Name of the away team.

  HomeGoals
      number of goals scored by the home team.

  AwayGoals
      number of goals scored by the away team.

  Round
      round of the game.

  Year
      year in which the season started.

  Date
      starting time of the game (in `"POSIXct"` format).

  Homepage of the Deutscher Fussball-Bund (DFB, German Football
  Association): http://www.dfb.de/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bundesliga.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 14018 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bundesliga.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Bundesliga.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bundesliga.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
