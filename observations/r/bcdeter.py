# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bcdeter(path):
  """data from Section 1.18

  The `bcdeter` data frame has 92 rows and 3 columns.

  This data frame contains the following columns:

  lower
      Lower limit of interval, months

  upper
      Upper limit of interval, months

  treat
      Treatment regimen (1=radiotherapy only, 2=radiotherapy +
      chemotherapy)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Beadle et al Cancer 54 (1984):2911-2918.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bcdeter.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 95 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bcdeter.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/bcdeter.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bcdeter.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
