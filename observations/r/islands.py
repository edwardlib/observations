# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def islands(path):
  """Areas of the World's Major Landmasses

  The areas in thousands of square miles of the landmasses which exceed
  10,000 square miles.

  A named vector of length 48.

  The World Almanac and Book of Facts, 1975, page 406.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `islands.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'islands.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/islands.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='islands.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
