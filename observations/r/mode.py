# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mode(path):
  """Mode Choice

  a cross-section

  *number of observations* : 453

  *observation* : individuals

  A dataframe containing :

  choice
      one of car, carpool, bus or rail

  cost.z
      cost of mode z

  time.z
      time of mode z

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mode.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 453 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mode.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Mode.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mode.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
