# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lifeboats(path):
  """Lifeboats on the Titanic

  Data from Mersey (1912) about the 18 (out of 20) lifeboats launched
  before the sinking of the S. S. Titanic.

  A data frame with 18 observations and 8 variables.

  launch
      launch time in `"POSIXt"` format.

  side
      factor. Side of the boat.

  boat
      factor indicating the boat.

  crew
      number of male crew members on board.

  men
      number of men on board.

  women
      number of women (including female crew) on board.

  total
      total number of passengers.

  cap
      capacity of the boat.

  M. Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/lifeboat.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lifeboats.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lifeboats.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Lifeboats.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lifeboats.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
