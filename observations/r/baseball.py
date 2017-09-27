# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def baseball(path):
  """Yearly batting records for all major league baseball players

  This data frame contains batting statistics for a subset of players
  collected from http://www.baseball-databank.org/. There are a total of
  21,699 records, covering 1,228 players from 1871 to 2007. Only players
  with more 15 seasons of play are included.

  A 21699 x 22 data frame

  Variables
  ~~~~~~~~~

  Variables:

  -  id, unique player id

  -  year, year of data

  -  stint

  -  team, team played for

  -  lg, league

  -  g, number of games

  -  ab, number of times at bat

  -  r, number of runs

  -  h, hits, times reached base because of a batted, fair ball without
     error by the defense

  -  X2b, hits on which the batter reached second base safely

  -  X3b, hits on which the batter reached third base safely

  -  hr, number of home runs

  -  rbi, runs batted in

  -  sb, stolen bases

  -  cs, caught stealing

  -  bb, base on balls (walk)

  -  so, strike outs

  -  ibb, intentional base on balls

  -  hbp, hits by pitch

  -  sh, sacrifice hits

  -  sf, sacrifice flies

  -  gidp, ground into double play

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `baseball.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21699 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'baseball.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plyr/baseball.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='baseball.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
