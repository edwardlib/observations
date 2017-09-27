# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nsw74psid_a(path):
  """A Subset of the nsw74psid1 Data Set

  The `nsw74psidA` data frame has 252 rows and 10 columns. See
  `nsw74psid1` for more information.

  This data frame contains the following columns:

  trt
      a numeric vector

  age
      a numeric vector

  educ
      a numeric vector

  black
      a numeric vector

  hisp
      a numeric vector

  marr
      a numeric vector

  nodeg
      a numeric vector

  re74
      a numeric vector

  re75
      a numeric vector

  re78
      a numeric vector

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nsw74psid_a.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 252 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nsw74psid_a.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nsw74psidA.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nsw74psid_a.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
