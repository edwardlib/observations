# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def public_schools(path):
  """US Expenditures for Public Schools

  Per capita expenditure on public schools and per capita income by state
  in 1979.

  A data frame containing 51 observations of 2 variables.

  Expenditure
      per capita expenditure on public schools,

  Income
      per capita income.

  Table 14.1 in Greene (1993)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `public_schools.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'public_schools.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/sandwich/PublicSchools.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='public_schools.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
