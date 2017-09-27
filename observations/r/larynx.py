# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def larynx(path):
  """data from Section 1.8

  The `larynx` data frame has 90 rows and 5 columns.

  This data frame contains the following columns:

  stage
      Stage of disease (1=stage 1, 2=stage2, 3=stage 3, 4=stage 4)

  time
      Time to death or on-study time, months

  age
      Age at diagnosis of larynx cancer

  diagyr
      Year of diagnosis of larynx cancer

  delta
      Death indicator (0=alive, 1=dead)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Kardaun Stat. Nederlandica 37 (1983),
  103-126.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `larynx.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'larynx.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/larynx.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='larynx.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
