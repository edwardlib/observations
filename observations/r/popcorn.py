# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def popcorn(path):
  """Popcorn

  Unpopped kernels in bags of microwave popcorn

  A dataset with 12 observations on the following 3 variables.

  `Unpopped`

  Number of unpopped kernels (adjusted for size difference

  `Brand`

  `Orville` or `Seaway`

  `Trial`

  Trial number


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `popcorn.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'popcorn.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Popcorn.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='popcorn.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
