# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_acc_deaths(path):
  """Accidental Deaths in the US 1973–1978

  A time series giving the monthly totals of accidental deaths in the USA.
  The values for the first six months of 1979 are 7798 7406 8363 8460 9217
  9316.

  P. J. Brockwell and R. A. Davis (1991) *Time Series: Theory and

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_acc_deaths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_acc_deaths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/USAccDeaths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_acc_deaths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
