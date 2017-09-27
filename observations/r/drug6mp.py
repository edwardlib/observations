# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def drug6mp(path):
  """data from Section 1.2

  The `drug6mp` data frame has 21 rows and 5 columns.

  This data frame contains the following columns:

  pair
      pair number

  remstat
      Remission status at randomization (1=partial, 2=complete)

  t1
      Time to relapse for placebo patients, months

  t2
      Time to relapse for 6-MP patients, months

  relapse
      Relapse indicator (0=censored, 1=relapse) for 6-MP patients

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Freireich et al. (1963) *Blood* 21:
  699-716.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `drug6mp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'drug6mp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/drug6mp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='drug6mp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
