# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sandwich_ants(path):
  """Sandwich Ants

  Ant counts on samples of different sandwiches

  A dataset with 48 observations on the following 5 variables.

  `Trial`

  Trial number

  `Bread`

  Type of bread: `Multigrain`, `Rye`, `White`, or `Wholemeal`

  `Filling`

  Type of filling: `HamPickles`, `PeanutButter`, or `Vegemite`

  `Butter`

  Butter on the sandwich? `no` or `yes`

  `Ants`

  Number of ants on the sandwich

  | Margaret Mackisack, “Favourite Experiments: An Addendum to What is the
    Use of Experiments Conducted by Statistics Students?", Journal of
    Statistics Education (1994)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sandwich_ants.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sandwich_ants.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/SandwichAnts.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sandwich_ants.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
