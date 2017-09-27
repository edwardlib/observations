# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sample_fg(path):
  """SampleFG

  A sample of 30 field goal attempts in the National Football League

  A dataset with 30 observations on the following 13 variables.

  `ID`

  ID number

  `PlayerID`

  Code for player

  `LastName`

  Last name

  `FirstName`

  First name

  `Year`

  Year

  `Team`

  Abbreviation for team name

  `Date`

  Code for date: mmdddyy

  `FGAttempts`

  Field goals attempted by the kicker that game

  `FGMade`

  Field goals made by the kicker that game

  `Attempt`

  Which attempt during the game?

  `Result`

  `1`\ =made the field goal or `0`\ =missed

  `Yards`

  Number of yards for the field goal attempt

  `Block`

  `1`\ =attempt blocked or `0`\ =not blocked

  We thank Sean Forman and Doug Drinen of Sports Reference LLC for

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sample_fg.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sample_fg.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/SampleFG.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sample_fg.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
