# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def psych(path):
  """data from Section 1.15

  The `psych` data frame has 927 rows and 10 columns.

  This data frame contains the following columns:

  sex
      Patient sex (1=male, 2=female)

  age
      Patient age

  time
      Time to death or on-study time

  death
      Death indicator (0=alive, 1=dead)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Woolsen Biometrics 37 (1981): 687-696.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `psych.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'psych.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/psych.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='psych.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
