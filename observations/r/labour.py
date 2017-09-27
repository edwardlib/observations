# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def labour(path):
  """Belgian Firms

  a cross-section from 1996

  *number of observations* : 569

  *observation* : production units

  *country* : Belgium

  A dataframe containing :

  capital
      total fixed assets, end of 1995 (in 1000000 euro)

  labour
      number of workers (employment)

  output
      value added (in 1000000 euro)

  wage
      wage costs per worker (in 1000 euro)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `labour.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 569 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'labour.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Labour.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='labour.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
