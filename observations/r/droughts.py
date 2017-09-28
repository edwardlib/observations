# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def droughts(path):
  """Periods Between Rain Events

  Data collected at Winnipeg International Airport (Canada) on periods (in
  days) between rain events.

  This data frame contains the following columns:

  length
      the length of time from the completion of the last rain event to the
      beginning of the next rain event.

  year
      the calendar year.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `droughts.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2042 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'droughts.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/droughts.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='droughts.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
