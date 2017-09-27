# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dimes(path):
  """Weight of dimes

  Weights of a sample of dimes.

  A data frame with 30 observations on the following 2 variables.

  -  `mass` mass of dime in grams

  -  `year` year the dime was minted


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dimes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dimes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Dimes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dimes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
