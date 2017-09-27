# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def banking_crises(path):
  """Countries in Banking Crises

  A `data.frame` identifying which of 70 countries had a banking crisis
  each year 1800:2010. The first column is `year`. The remaining columns
  carry the names of the countries; those columns are 1 for years with
  banking crises and 0 otherwise.

  A `data.frame`

  http://www.reinhartandrogoff.com

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `banking_crises.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 211 rows and 71 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'banking_crises.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/bankingCrises.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='banking_crises.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
