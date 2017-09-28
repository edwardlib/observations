# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def forward(path):
  """Exchange Rates of US Dollar Against Other Currencies

  monthly observations from 1979–01 to 2001–12

  *number of observations* : 276

  A time serie containing :

  usdbp
      exchange rate USD/British Pound Sterling

  usdeuro
      exchange rate US D/Euro

  eurobp
      exchange rate Euro/Pound

  usdbp1
      1 month forward rate USD/Pound

  usdeuro1
      1 month forward rate USD/Euro

  eurobp1
      1 month forward rate Euro/Pound

  usdbp3
      3 month forward rate USD/Pound

  usdeuro3
      month forward rate USD/Euro

  eurobp3
      month forward rate Euro/Pound

  Datastream .

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `forward.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 276 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'forward.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Forward.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='forward.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
