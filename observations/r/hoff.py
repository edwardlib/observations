# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hoff(path):
  """Social Security Expenditure Data

  This data set contains annual social security expenditure (as percent of
  budget lagged by two years), the relative frequency of mentions social
  justice received in the party's platform in each year, and whether the
  president is Republican or Democrat.

  A table containing 5 variables ("year", "L2SocSec", "Just503D",
  "Just503R", "RGovDumy") and 36 observations.

  ICPSR (replication dataset s1109)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hoff.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hoff.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/hoff.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hoff.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
