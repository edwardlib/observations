# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def telef(path):
  """Number of International Calls from Belgium

  Number of international calls from Belgium, taken from the Belgian
  Statistical Survey, published by the Ministry of Economy.

  A data frame with 24 observations on the following 2 variables.

  `Calls`
      Number of Calls (in tens of millions)

  `Year`
      Year (1950 - 1973)

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, page 26, table 2.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `telef.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'telef.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/telef.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='telef.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
