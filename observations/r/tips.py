# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tips(path):
  """Tipping data

  One waiter recorded information about each tip he received over a period
  of a few months working in one restaurant. He collected several
  variables:

  A data frame with 244 rows and 7 variables

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tips.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 244 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tips.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/reshape2/tips.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tips.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
