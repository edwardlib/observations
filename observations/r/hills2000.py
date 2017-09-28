# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hills2000(path):
  """Scottish Hill Races Data - 2000

  The record times in 2000 for 56 Scottish hill races. We believe the data
  are, for the most part, trustworthy. This is the subset of `races2000`
  for which `type` is `hill`.

  This data frame contains the following columns:

  dist
      distance, in miles (on the map)

  climb
      total height gained during the route, in feet

  time
      record time in hours

  timef
      record time in hours for females

  The Scottish Running Resource, http://www.hillrunning.co.uk

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hills2000.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hills2000.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/hills2000.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hills2000.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
