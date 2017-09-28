# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def orings1(path):
  """Orings

  Number of damaged O-rings on space shuttle launches and launch
  temperature

  A dataset with 24 observations on the following 2 variables.

  `Temp`

  Code for temperature (in degrees F): `Above65` `Below65`

  `Failures`

  Number of O-ring failures

  Data can be found in "Risk analysis of the space shuttle: Pre-challenger
  prediction of failure" by Siddhartha R. Dalal, Edward B. Fowlke, and
  Bruce Hoadley in Journal of the American Statistical Association, Vol.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `orings1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'orings1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Orings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='orings1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
