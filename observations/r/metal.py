# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def metal(path):
  """Production for SIC 33

  a cross-section

  *number of observations* : 27

  *observation* : regional

  *country* : United States

  A dataframe containing :

  va
      output

  labor
      labor input

  capital
      capital input

  Aigner, D., K. Lovell and P. Schmidt (1977) “Formulation and estimation
  of stochastic frontier production models”, *Journal of Econometrics*,
  **6**, 21-37.

  Hildebrand, G. and T. Liu (1957) *Manufacturing production functions in
  the United States*, Ithaca, N.Y.: Cornell University Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `metal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'metal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Metal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='metal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
