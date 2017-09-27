# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sp500_close(path):
  """Closing Numbers for S and P 500 Index

  Closing numbers for S and P 500 Index, Jan. 1, 1990 through early 2000.

  Derived from SP500 in the MASS library.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sp500_close.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2780 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sp500_close.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/SP500close.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sp500_close.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
