# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hoops(path):
  """Hoops

  Hoops

  A dataset with 147 observations on the following 22 variables.

  `Game`

  An ID number assigned to each game

  `Opp`

  Name of the opponent school for the game

  `Home`

  Indicator variable where `1` = home game and `0` = away game

  `OppAtt`

  Number of field goal attempts by the opposing team

  `GrAtt`

  Number of field goal attempts by Grinnell

  `Gr3Att`

  Number of three-point field goal attempts by Grinnell

  `GrFT`

  Number of free throw attempts by Grinnell

  `OppFT`

  Number of free throw attempts by the opponent

  `GrRB`

  Total number of Grinnell rebounds

  `GrOR`

  Number of Grinnell offensive rebounds

  `OppDR`

  Number of defensive rebounds the opposing team had

  `OppPoint`

  Points scored in the game by the opponent

  `GrPoint`

  Points scored in the game by Grinnell

  `GrAss`

  Number of assists Grinnell had in the game

  `OppTO`

  Number of turnovers the opposing team gave up

  `GrTO`

  Number of turnovers Grinnell gave up

  `GrBlocks`

  Number of blocks Grinnell had in the game

  `GrSteal`

  Number of steals Grinnell had in the game

  `X40Point`

  Indicator variable that is 1 if some Grinnell player scored 40 or more
  points

  `X30Point`

  Indicator variable that is 1 if some Grinnell player scored 30 or more
  points

  `WinLoss`

  `1`\ =Grinnell win or `0`\ =Grinnell loss

  `PtDiff`

  Point differential for the game (Grinnell score minus Opponent's score)

  These data were collected by Grinnell College students Eric Ohrn and Ben

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hoops.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 147 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hoops.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Hoops.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hoops.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
