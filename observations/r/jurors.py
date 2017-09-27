# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def jurors(path):
  """Jurors

  Jurors

  A dataset with 52 observations on the following 4 variables.

  `Period`

  Sequential 2-week periods ove the course of a year

  `PctReport`

  Percentage of selected jurors who report

  `Year`

  `1998` or `2000`

  `I2000`

  Indicator for data from the year 2000


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `jurors.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 52 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'jurors.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Jurors.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='jurors.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
