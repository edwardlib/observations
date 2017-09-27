# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def titanicgrp(path):
  """titanicgrp

  The data is an grouped version of the 1912 Titanic passenger survival
  log,

  A data frame with 12 observations on the following 5 variables.

  `survive`
      number of passengers who survived

  `cases`
      number of passengers with same pattern of covariates

  `age`
      1=adult; 0=child

  `sex`
      1=Male; 0=female

  `class`
      ticket class 1= 1st class; 2= second class; 3= third class

  Found in many other texts

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `titanicgrp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'titanicgrp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/titanicgrp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='titanicgrp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
