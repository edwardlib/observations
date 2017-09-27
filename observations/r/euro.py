# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def euro(path):
  """Conversion Rates of Euro Currencies

  Conversion rates between the various Euro currencies.

  `euro` is a named vector of length 11, `euro.cross` a matrix of size
  11 by 11, with dimnames.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `euro.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'euro.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/euro.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='euro.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
