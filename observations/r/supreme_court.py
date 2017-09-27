# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def supreme_court(path):
  """U.S. Supreme Court Vote Matrix

  This dataframe contains a matrix votes cast by U.S. Supreme Court
  justices in all cases in the 2000 term.

  The dataframe has contains data for justices Rehnquist, Stevens,
  O'Connor, Scalia, Kennedy, Souter, Thomas, Ginsburg, and Breyer for the
  2000 term of the U.S. Supreme Court. It contains data from 43
  non-unanimous cases. The votes are coded liberal (1) and conservative
  (0) using the protocol of Spaeth (2003). The unit of analysis is the
  case citation (ANALU=0). We are concerned with formally decided cases
  issued with written opinions, after full oral argument and cases decided
  by an equally divided vote (DECTYPE=1,5,6,7).

  Harold J. Spaeth (2005). “Original United States Supreme Court Database:
  1953-2004 Terms.”

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `supreme_court.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 43 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'supreme_court.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/SupremeCourt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='supreme_court.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
