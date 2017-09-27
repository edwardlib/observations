# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def transp_eq(path):
  """Statewide Data on Transportation Equipment Manufacturing

  a cross-section

  *number of observations* : 25

  *observation* : regional

  *country* : United States

  A dataframe containing :

  state
      state name

  va
      output

  capital
      capital input

  labor
      labor input

  nfirm
      number of firms

  Zellner, A. and N. Revankar (1970) “Generalized production functions”,
  *Review of Economic Studies*, **37**, 241-250.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `transp_eq.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'transp_eq.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/TranspEq.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='transp_eq.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
