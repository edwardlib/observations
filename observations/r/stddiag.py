# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def stddiag(path):
  """data from Exercise 5.6, p146

  The `stddiag` data frame has 25 rows and 2 columns.

  This data frame contains the following columns:

  encounter
      Months from 1/93 to encounter

  diagnosed
      Months until STD diagnosed in the clinic

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `stddiag.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'stddiag.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/stddiag.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='stddiag.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
