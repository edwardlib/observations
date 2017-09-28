# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def backpack(path):
  """Backpack

  Backpack weights for a sample of college students

  A dataset with 100 observations on the following 9 variables.

  `BackpackWeight`

  Backpack weight (in pounds)

  `BodyWeight`

  Body weight (in pounds)

  `Ratio`

  BackpackWeight/BodyWeight

  `BackProblems`

  0=no or 1=yes

  `Major`

  Code for academic major

  `Year`

  Year in school

  `Sex`

  a factor with levels `Female` `Male`

  `Status`

  Graduate or undergraduate? `G` or `U`

  `Units`

  Number of credits taken that quarter

  Mintz J., Mintz J., Moore K., and Schuh K., "Oh, My Aching Back! A
  Statistical Analysis of Backpack Weights," Stats: The Magazine for

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `backpack.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'backpack.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Backpack.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='backpack.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
