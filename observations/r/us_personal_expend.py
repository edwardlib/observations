# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_personal_expend(path):
  """Personal Expenditure Data

  This data set consists of United States personal expenditures (in
  billions of dollars) in the categories; food and tobacco, household
  operation, medical and health, personal care, and private education for
  the years 1940, 1945, 1950, 1955 and 1960.

  A matrix with 5 rows and 5 columns.

  The World Almanac and Book of Facts, 1962, page 756.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_personal_expend.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_personal_expend.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/USPersonalExpenditure.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_personal_expend.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
