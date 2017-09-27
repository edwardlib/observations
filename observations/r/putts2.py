# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def putts2(path):
  """Putts2

  Putting results for a golfing statistician (by length of the putts)

  A dataset with 5 observations on the following 4 variables.

  `Length`

  Length of the attempted putt (in feet)

  `Made`

  Number of putts made at this length

  `Missed`

  Number of putts missed at this length

  `Trials`

  Total number of putts attempted at this length


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `putts2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'putts2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Putts2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='putts2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
