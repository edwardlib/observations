# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def approval(path):
  """U.S. Presidential Approval Data

  Monthy public opinion data for 2001-2006.

  A table containing 8 variables ("month", "year", "approve",
  "disapprove", "unsure", "sept.oct.2001", "iraq.war", and "avg.price")
  and 65 observations.

  ICPSR

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `approval.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 65 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'approval.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/approval.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='approval.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
