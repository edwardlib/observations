# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def city(path):
  """Population of U.S. Cities

  The `bigcity` data frame has 49 rows and 2 columns.

  The `city` data frame has 10 rows and 2 columns.

  The measurements are the population (in 1000's) of 49 U.S. cities in
  1920 and 1930. The 49 cities are a random sample taken from the 196
  largest cities in 1920. The `city` data frame consists of the first 10
  observations in `bigcity`.

  This data frame contains the following columns:

  `u`
      The 1920 population.

  `x`
      The 1930 population.

  The data were obtained from

  Cochran, W.G. (1977) *Sampling Techniques*. Third edition. John Wiley

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `city.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'city.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/city.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='city.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
