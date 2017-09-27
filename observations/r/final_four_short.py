# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def final_four_short(path):
  """FinalFourShort

  NCAA Final Four by seed - short version

  A dataset with 512 observations on the following 4 variables.

  `Year`

  Year: 1979 to 2010

  `Seed`

  Seed: 1 to 16

  `In`

  Number of teams at that seed who made the Final Four that year

  `Out`

  Number of teams at that seed who did not made the Final Four that year

  Final Four teams and their seed can be found at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `final_four_short.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 512 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'final_four_short.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FinalFourShort.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='final_four_short.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
