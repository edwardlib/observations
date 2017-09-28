# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def swim_records(path):
  """100 m Swimming World Records

  World records for men and women over time from 1905 through 2004.

  A data frame with 62 observations of the following variables.

  -  `time` time (in seconds) of the world record

  -  `year` Year in which the record was set

  -  `sex` a factor with levels `M` and `F`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `swim_records.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'swim_records.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/SwimRecords.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='swim_records.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
