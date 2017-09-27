# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def baboon(path):
  """data from Exercise 5.8, p147

  The `baboon` data frame has 25 rows and 2 columns.

  This data frame contains the following columns:

  date
      Date (day/month/year)

  time
      Descent time (military time)

  observed
      Indicator of observed or not (1=observed, 0=not observed)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `baboon.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 152 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'baboon.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/baboon.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='baboon.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
