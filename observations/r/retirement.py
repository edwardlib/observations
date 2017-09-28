# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def retirement(path):
  """Retirement

  Contributions to a supplemental retirement account (1997-2012)

  A dataset with 16 observations on the following 2 variables.

  `Year`

  1997-2012

  `SRA`

  Annual contribution to the Supplemental Retirement Account


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `retirement.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'retirement.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Retirement.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='retirement.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
