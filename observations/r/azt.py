# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def azt(path):
  """data from Exercise 4.7, p122

  The `azt` data frame has 45 rows and 4 columns.

  This data frame contains the following columns:

  patient
      Patient number

  ageentry
      Age at entry into AZT study, months

  age
      Age at death or censoring time, months

  death
      Death indicator (1=dead, 0=alive)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `azt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'azt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/azt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='azt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
