# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mlb_2007_standings(path):
  """MLB2007Standings

  Data for Major League Baseball teams from the 2007 regular season

  A dataset with 30 observations on the following 21 variables.

  `Team`

  Name of the team

  `League`

  League: `AL` or `NL`

  `Wins`

  Number of wins for the season (out of 162 games)

  `Losses`

  Number of losses for the season

  `WinPct`

  Proportion of games won (Wins/162)

  `BattingAvg`

  Team batting average

  `Runs`

  Number of runs runs scored

  `Hits`

  Number of hits

  `HR`

  Number of home runs hit

  `Doubles`

  Number of doubles hit

  `Triples`

  Number of triple hit

  `RBI`

  Number of runs batted in

  `SB`

  Number of stoen bases

  `OBP`

  On base percentage

  `SLG`

  Slugging percentage

  `ERA`

  Earned run average (earned runs allowed per 9 innings)

  `HitsAllowed`

  Number of hits against the team

  `Walks`

  Number of walks allowed

  `StrikeOuts`

  Number of strikeouts (by the team's pitchers)

  `Saves`

  Number of games saved (by the team's pitchers

  `WHIP`

  Number of walks and hits per inning pitched

  | Data downloaded from baseball-reference.com:
  | http://www.baseball-reference.com/leagues/MLB/2007-standings.shtml

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mlb_2007_standings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 21 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mlb_2007_standings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MLB2007Standings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mlb_2007_standings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
