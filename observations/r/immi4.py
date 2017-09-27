# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def immi4(path):
  """Individual Preferences Over Immigration Policy

  These five datasets are part of a larger set of 10 multiply imputed data
  sets describing individual preferences toward immigration policy.
  Imputation was performed via Amelia.

  Each multiply-inputed data set consists of a table with 7 variables
  ("ipip", "wage1992", "prtyid", "ideol", "gender") and 2,485
  observations. For variable descriptions, please refer to Scheve and
  Slaugher, 2001.

  National Election Survey

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `immi4.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2485 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'immi4.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/immi4.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='immi4.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
