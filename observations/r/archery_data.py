# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def archery_data(path):
  """ArcheryData

  Score results from an archery class

  A dataset with 18 observations on the following 7 variables.

  `Attendance`

  Number of days in class

  `Average`

  Average score over all days

  `Sex`

  Coded as `f` or `m`

  `Day1`

  Archery score on first day

  `LastDay`

  Archery score on last day

  `Improvement`

  Last day - first day score

  `Improve`

  1=improved or 0= did not improve


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `archery_data.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'archery_data.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/ArcheryData.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='archery_data.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
