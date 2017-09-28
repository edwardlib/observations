# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def discoveries(path):
  """Yearly Numbers of Important Discoveries

  The numbers of “great” inventions and scientific discoveries in each
  year from 1860 to 1959.

  A time series of 100 values.

  The World Almanac and Book of Facts, 1975 Edition, pages 315–318.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `discoveries.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'discoveries.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/discoveries.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='discoveries.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
