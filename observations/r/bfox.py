# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bfox(path):
  """Canadian Women's Labour-Force Participation

  The `Bfox` data frame has 30 rows and 7 columns. Time-series data on
  Canadian women's labor-force participation, 1946–1975.

  This data frame contains the following columns:

  partic
      Percent of adult women in the workforce.

  tfr
      Total fertility rate: expected births to a cohort of 1000 women at
      current age-specific fertility rates.

  menwage
      Men's average weekly wages, in constant 1935 dollars and adjusted
      for current tax rates.

  womwage
      Women's average weekly wages.

  debt
      Per-capita consumer debt, in constant dollars.

  parttime
      Percent of the active workforce working 34 hours per week or less.

  Warning
  ~~~~~~~

  The value of `tfr` for 1973 is misrecorded as 2931; it should be 1931.

  Fox, B. (1980) *Women's Domestic Labour and their Involvement in Wage
  Work.* Unpublished doctoral dissertation, p. 449.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bfox.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bfox.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Bfox.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bfox.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
