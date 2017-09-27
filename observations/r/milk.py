# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def milk(path):
  """Milk Sweetness Study

  The `milk` data frame has 17 rows and 2 columns. Each of 17 panelists
  compared two milk samples for sweetness.

  This data frame contains the following columns:

  four
      a numeric vector consisting of the assessments for four units of
      additive

  one
      a numeric vector while the is the assessment for one unit of
      additive

  J.H. Maindonald

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `milk.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 86 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'milk.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/milk.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='milk.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
