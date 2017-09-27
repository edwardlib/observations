# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def weldon_dice(path):
  """Weldon's Dice Data

  Data from Pearson (1900) about the frequency of 5s and 6s in throws of
  12 dice. Weldon tossed the dice 26,306 times and reported his results in
  a letter to Francis Galton on 1894-02-02.

  A 1-way table giving the frequency of a 5 or a 6 in 26,306 throws of 12
  dice where 10 indicates ‘10 or more’ 5s or 6s. The variable and its
  levels are

  No

  Name

  Levels

  1

  n56

  0, 1, ..., 10

  M. Friendly (2000), Visualizing Categorical Data, pages 20–21.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `weldon_dice.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'weldon_dice.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/WeldonDice.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='weldon_dice.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
