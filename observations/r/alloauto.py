# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def alloauto(path):
  """data from Section 1.9

  The `alloauto` data frame has 90 rows and 5 columns.

  This data frame contains the following columns:

  time
      Time to death or relapse, months

  type
      Type of transplant (1=allogeneic, 2=autologous)

  delta
      Leukemia-free survival indicator (0=alive without relapse, 1=dead or
      relapse)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Kardaun Stat. Nederlandica 37 (1983),
  103-126.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `alloauto.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 101 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'alloauto.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/alloauto.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='alloauto.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
