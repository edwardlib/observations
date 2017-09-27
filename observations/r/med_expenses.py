# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def med_expenses(path):
  """Family Medical Expenses

  The `medExpenses` data frame contains average weekly medical expenses
  including drugs for 33 families randomly sampled from a community of 600
  families which contained 2700 individuals. These data were collected in
  the 1970's at an unknown location.

  familysize
      number of individuals in a family

  expenses
      average weekly cost for medical expenses per family member

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `med_expenses.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 33 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'med_expenses.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/medExpenses.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='med_expenses.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
