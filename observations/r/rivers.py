# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rivers(path):
  """Lengths of Major North American Rivers

  This data set gives the lengths (in miles) of 141 “major” rivers in
  North America, as compiled by the US Geological Survey.

  A vector containing 141 observations.

  World Almanac and Book of Facts, 1975, page 406.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rivers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 141 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rivers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/rivers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rivers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
