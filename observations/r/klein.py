# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def klein(path):
  """Klein's Model I

  annual observations from 1920 to 1941

  *number of observations* : 22

  *observation* : country

  *country* : United States

  A time serie containing :

  cons
      consumption

  profit
      corporate profits

  privwage
      private wage bill

  inv
      investment

  lcap
      previous year's capital stock

  gnp
      GNP

  pubwage
      government wage bill

  govspend
      government spending

  taxe
      taxes

  Klein, L. (1950) *Economic fluctuations in the United States,
  1921-1941*, New York, John Wiley and Sons.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `klein.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'klein.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Klein.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='klein.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
