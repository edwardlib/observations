# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def produc(path):
  """Us States Production

  a panel of 48 observations from 1970 to 1986

  *number of observations* : 816

  *observation* : regional

  *country* : United States

  A dataframe containing :

  state
      the state

  year
      the year

  pcap
      private capital stock

  hwy
      highway and streets

  water
      water and sewer facilities

  util
      other public buildings and structures

  pc
      public capital

  gsp
      gross state products

  emp
      labor input measured by the employment in non–agricultural payrolls

  unemp
      state unemployment rate

  Munnell, A. (1990) “Why has productivity growth declined? Productivity
  and public investment”, *New England Economic Review*, 3–22.

  Baltagi, B. H. and N. Pinnoi (1995) “Public capital stock and state
  productivity growth: further evidence”, *Empirical Economics*, **20**,
  351–359.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `produc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 816 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'produc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Produc.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='produc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
