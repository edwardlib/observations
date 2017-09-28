# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mexico(path):
  """Voting Data from the 1988 Mexican Presidental Election

  This dataset contains voting data for the 1988 Mexican presidential
  election.

  A table containing 33 variables and 1,359 observations.

  ICPSR

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mexico.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1359 rows and 33 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mexico.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/mexico.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mexico.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
