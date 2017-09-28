# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def geyser(path):
  """Old Faithful Geyser Data

  A version of the eruptions data from the ‘Old Faithful’ geyser in
  Yellowstone National Park, Wyoming. This version comes from Azzalini and
  Bowman (1990) and is of continuous measurement from August 1 to August
  15, 1985.

  Some nocturnal duration measurements were coded as 2, 3 or 4 minutes,
  having originally been described as ‘short’, ‘medium’ or ‘long’.

  A data frame with 299 observations on 2 variables.

  `duration`

  numeric

  Eruption time in mins

  `waiting`

  numeric

  Waiting time for this eruption

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `geyser.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 299 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'geyser.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/geyser.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='geyser.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
