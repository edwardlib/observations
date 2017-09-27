# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bids(path):
  """Bids Received By U.S. Firms

  a cross-section

  *number of observations* : 126

  *observation* : production units

  *country* : United States

  A dataframe containing :

  docno
      doc no.

  weeks
      weeks

  numbids
      count

  takeover
      delta (1 if taken over)

  bidprem
      bid Premium

  insthold
      institutional holdings

  size
      size measured in billions

  leglrest
      legal restructuring

  rearest
      real restructuring

  finrest
      financial restructuring

  regulatn
      regulation

  whtknght
      white knight

  Jaggia, Sanjiv and Satish Thosar (1993) “Multiple Bids as a Consequence
  of Target Management Resistance”, *Review of Quantitative Finance and
  Accounting*, 447–457.

  Cameron, A.C. and Per Johansson (1997) “Count Data Regression Models
  using Series Expansions: with Applications”, *Journal of Applied
  Econometrics*, **12**, may, 203–223.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bids.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 126 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bids.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Bids.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bids.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
