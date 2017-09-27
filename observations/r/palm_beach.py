# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def palm_beach(path):
  """PalmBeach

  Votes for Geroge Bush and Pat Buchanan in Florida counties for the 2000
  U.S. presidential election

  A dataset with 67 observations on the following 3 variables.

  `County`

  Name of the Florida county

  `Buchanan`

  Number of votes for Par Buchanan

  `Bush`

  number of votes for George Bush

  Florida county data for the 2000 presidential election can be found at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `palm_beach.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 67 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'palm_beach.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/PalmBeach.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='palm_beach.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
