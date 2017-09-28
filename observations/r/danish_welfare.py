# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def danish_welfare(path):
  """Danish Welfare Study Data

  Data from the Danish Welfare Study.

  A data frame with 180 observations and 5 variables.

  Freq
      frequency.

  Alcohol
      factor indicating daily alcohol consumption: less than 1 unit (<1),
      1-2 units (1-2) or more than 2 units (>2). 1 unit is approximately 1
      bottle of beer or 4cl 40% alcohol.

  Income
      factor indicating income group in 1000 DKK (0-50, 50-100, 100-150,
      >150).

  Status
      factor indicating marriage status (Widow, Married, Unmarried).

  Urban
      factor indicating urbanization: Copenhagen (Copenhagen), Suburbian
      Copenhagen (SubCopenhagen), three largest cities (LargeCity), other
      cities (City), countryside (Country).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  page 205.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `danish_welfare.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 180 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'danish_welfare.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/DanishWelfare.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='danish_welfare.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
