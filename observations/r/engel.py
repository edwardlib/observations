# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def engel(path):
  """Engel Data

  Engel food expenditure data used in Koenker and Bassett(1982). This is a
  regression data set consisting of 235 observations on income and
  expenditure on food for Belgian working class households.

  A data frame containing 235 observations on 2 variables

  income
      annual household income in Belgian francs

  foodexp
      annual household food expenditure in Belgian francs

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `engel.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 235 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'engel.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/quantreg/engel.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='engel.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
