# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def default(path):
  """Credit Card Default Data

  A simulated data set containing information on ten thousand customers.
  The aim here is to predict which customers will default on their credit
  card debt.

  A data frame with 10000 observations on the following 4 variables.

  `default`
      A factor with levels `No` and `Yes` indicating whether the
      customer defaulted on their debt

  `student`
      A factor with levels `No` and `Yes` indicating whether the
      customer is a student

  `balance`
      The average balance that the customer has remaining on their credit
      card after making their monthly payment

  `income`
      Income of customer

  Simulated data

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `default.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10000 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'default.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Default.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='default.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
