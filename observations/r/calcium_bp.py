# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def calcium_bp(path):
  """CalciumBP

  Calcium and blood pressure

  A dataset with 21 observations on the following 2 variables.

  `Treatment`

  `Calcium` or `Placebo`

  `Decrease`

  Beginning-ending blood pressure

  | Dataset downloaded from online data source Data and Story Library,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `calcium_bp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'calcium_bp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/CalciumBP.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='calcium_bp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
