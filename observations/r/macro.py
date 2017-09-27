# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def macro(path):
  """Macroeconomic Data

  Selected macroeconomic indicators for Austria, Belgium, Canada, Denmark,
  Finland, France, Italy, Japan, the Netherlands, Norway, Sweden, the
  United Kingdom, the United States, and West Germany for the period
  1966-1990.

  A table containing 6 variables ("country", "year", "gdp", "unem",
  "capmob", and "trade") and 350 observations.

  ICPSR

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `macro.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 350 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'macro.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/macro.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='macro.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
