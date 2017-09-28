# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def high_peaks(path):
  """HighPeaks

  Adirondack High Peaks

  A dataset with 46 observations on the following 6 variables.

  `Peak`

  Name of the mountain

  `Elevation`

  Elevation at the highest point (in feet)

  `Difficulty`

  Rating of difficulty of the hike: `1` (easy) to `7` (most difficult)

  `Ascent`

  Vertical ascent (in feet)

  `Length`

  Length of hike (in miles)

  `Time`

  Expected trip time (in hours)

  High Peaks data avaialble at
  http://www.adirondack.net/tour/hike/highpeaks.cfm. Thanks to Jessica

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `high_peaks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 46 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'high_peaks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/HighPeaks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='high_peaks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
