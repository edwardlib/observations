# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cp_sch3(path):
  """Earnings from the Current Population Survey

  a cross-section from 1998

  *number of observations* : 11130

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  year
      survey year

  ahe
      average hourly earnings

  sex
      a factor with levels (male,female)

  Bureau of labor statistics, U.S. Department of Labor http://www.bls.gov.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cp_sch3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11130 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cp_sch3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/CPSch3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cp_sch3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
