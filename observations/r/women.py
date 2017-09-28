# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def women(path):
  """Average Heights and Weights for American Women

  This data set gives the average heights and weights for American women
  aged 30–39.

  A data frame with 15 observations on 2 variables.

  +------------+--------------+-----------+----------------+
  | `[,1]`   | `height`   | numeric   | Height (in)    |
  +------------+--------------+-----------+----------------+
  | `[,2]`   | `weight`   | numeric   | Weight (lbs)   |
  +------------+--------------+-----------+----------------+

  The World Almanac and Book of Facts, 1975.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `women.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'women.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/women.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='women.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
