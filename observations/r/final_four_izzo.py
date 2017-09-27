# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def final_four_izzo(path):
  """FinalFourIzzo

  NCAA Final Four by seed with indicator for Tom Izzo's teams

  A dataset with 1664 observations on the following 4 variables.

  `Year`

  Year 1985-2010

  `Seed`

  Seed in NCAA men's basketball tournament: 1 to 16

  `Final4`

  `1`\ =made Final Four or `0`\ =did not make Final Four

  `Izzo`

  `1`\ =team coached by Tom Izzo or `0`\ =not an Izzo team

  Final Four teams and their seed can be found at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `final_four_izzo.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1664 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'final_four_izzo.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FinalFourIzzo.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='final_four_izzo.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
