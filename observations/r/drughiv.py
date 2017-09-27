# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def drughiv(path):
  """data from Exercise 7.6, p222

  The `drughiv` data frame has 34 rows and 3 columns.

  This data frame contains the following columns:

  drug
      Drug combination (1=AZT + zalcitabine, 2=AZT + zalcitabine +
      saquinavir)

  time
      Time after drug administration to CD4 count at a specified level,
      days

  delta
      Indicator of CD4 count reaching specified level (1=yes, 0=no)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `drughiv.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 34 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'drughiv.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/drughiv.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='drughiv.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
