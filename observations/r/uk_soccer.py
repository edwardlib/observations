# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def uk_soccer(path):
  """UK Soccer Scores

  Data from Lee (1997), on the goals scored by Home and Away teams in the
  Premier Football League, 1995/6 season.

  A 2-dimensional array resulting from cross-tabulating the number of
  goals scored in 380 games. The variables and their levels are as
  follows:

  +------+--------+----------------+
  | No   | Name   | Levels         |
  +------+--------+----------------+
  | 1    | Home   | 0, 1, ..., 4   |
  +------+--------+----------------+
  | 2    | Away   | 0, 1, ..., 4   |
  +------+--------+----------------+

  M. Friendly (2000), Visualizing Categorical Data, page 27.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `uk_soccer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'uk_soccer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/UKSoccer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='uk_soccer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
