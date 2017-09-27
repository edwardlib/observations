# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rearrests(path):
  """Rearrests of Juvenile Felons

  Rearrests of juventile felons by type of court in which they were tried.

  A two-way classification, see `table`.

  A. Agresti (1996). *An Introduction to Categorical Data Analysis*.
  Wiley, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rearrests.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rearrests.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/rearrests.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rearrests.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
