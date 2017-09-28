# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def accdeaths(path):
  """Accidental Deaths in the US 1973-1978

  A regular time series giving the monthly totals of accidental deaths in
  the USA.

  P. J. Brockwell and R. A. Davis (1991) *Time Series: Theory and
  Methods.* Springer, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `accdeaths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'accdeaths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/accdeaths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='accdeaths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
