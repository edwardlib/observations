# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def smoking(path):
  """smoking

  A simple data set with only 6 observations.

  A data frame with 6 observations on the following 4 variables.

  `sbp`
      systolic blood pressure of subject

  `male`
      1=male; 0=female

  `smoker`
      1=hist of smoking; 0= no hist of smoking

  `age`
      age of subject

  none

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `smoking.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'smoking.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/smoking.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='smoking.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
