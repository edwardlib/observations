# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def electricity(path):
  """Cost Function for Electricity Producers

  a cross-section from 1970 to 1970

  *number of observations* : 158

  *observation* : production units

  *country* : United States

  A dataframe containing :

  cost
      total cost

  q
      total output

  pl
      wage rate

  sl
      cost share for labor

  pk
      capital price index

  sk
      cost share for capital

  pf
      fuel price

  sf
      cost share for fuel

  Christensen, L. and W. H. Greene (1976) “Economies of scale in U.S.
  electric power generation”, *Journal of Political Economy*, **84**,
  655-676.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `electricity.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 158 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'electricity.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Electricity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='electricity.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
