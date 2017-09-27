# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def allograft(path):
  """data from Exercise 13.1, p418

  The `allograft` data frame has 34 rows and 4 columns.

  This data frame contains the following columns:

  patient
      Patient

  time
      Time to graft rejection, days

  rejection
      Indicator of graft rejection (1=yes, 0=no)

  match
      Good HLA skin match (1=yes, 0=no)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Batchelor and Hackett Lancet 2 (1970):
  581-583.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `allograft.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 34 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'allograft.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/allograft.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='allograft.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
