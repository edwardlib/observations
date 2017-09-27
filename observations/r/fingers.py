# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fingers(path):
  """Fingers

  Fingers

  A dataset with 12 observations on the following 3 variables.

  `Subject`

  `I`, `II`, `III`, or `IV`

  `Drug`

  `Caffeine`, `Placebo`, or `Theobromine`

  `TapRate`

  Finger taps in a fixed time interval

  The data was found in Statistics in Biology, Vol. 1, by C. I. Bliss
  (1967), New York: McGraw Hill.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fingers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fingers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Fingers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fingers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
