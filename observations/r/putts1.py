# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def putts1(path):
  """Putts1

  Putting results for a golfing statistician

  A dataset with 587 observations on the following 2 variables.

  `Length`

  Length if the putt (in feet

  `Made`

  `1`\ =made the putt or `0`\ =missed the putt


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `putts1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 587 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'putts1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Putts1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='putts1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
