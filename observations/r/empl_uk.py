# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def empl_uk(path):
  """Employment and Wages in the United Kingdom

  An unbalanced panel of 140 observations from 1976 to 1984

  *total number of observations* : 1031

  *observation* : firms

  *country* : United Kingdom

  A data frame containing :

  firm
      firm index

  year
      year

  sector
      the sector of activity

  emp
      employment

  wage
      wages

  capital
      capital

  output
      output

  Arellano, M. and Bond, S. (1991), Some Tests of Specification for Panel
  Data: Monte Carlo Evidence and an Application to Employment Equations,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `empl_uk.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1031 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'empl_uk.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/EmplUK.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='empl_uk.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
