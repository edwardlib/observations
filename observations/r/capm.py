# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def capm(path):
  """Stock Market Data

  monthly observations from 1960–01 to 2002–12

  *number of observations* : 516

  A time serie containing :

  rfood
      excess returns food industry

  rdur
      excess returns durables industry

  rcon
      excess returns construction industry

  rmrf
      excess returns market portfolio

  rf
      riskfree return

  most of the above data are from Kenneth French's data library at
  http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `capm.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 516 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'capm.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Capm.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='capm.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
