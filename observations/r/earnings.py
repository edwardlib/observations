# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def earnings(path):
  """Earnings for Three Age Groups

  a cross-section from 1988-1989

  *number of observations* : 4266

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  age
      age groups, a factor with levels (g1,g2,g3)

  y
      average annual earnings, in 1982 US dollars

  Mills, Jeffery A. and Sourushe Zandvakili (1997) “Statistical Inference
  via Bootstrapping for Measures of Inequality”, *Journal of Applied
  Econometrics*, **12(2)**, pp. 133-150.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `earnings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4266 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'earnings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Earnings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='earnings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
