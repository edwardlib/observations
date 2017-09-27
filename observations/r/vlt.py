# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vlt(path):
  """Video Lottery Terminal Data

  Data on objects appearing in three windows on a video lottery terminal,
  together with the prize payout (usually 0). Observations were taken on
  two successive days in late 1994 at a hotel lounge north of Winnipeg,
  Manitoba. Each observation cost 25 cents (Canadian). The game played was
  ‘Double Diamond’.

  This data frame contains the following columns:

  window1
      object appearing in the first window.

  window2
      object appearing in the second window.

  window3
      object appearing in the third window.

  prize
      cash prize awarded (in Canadian dollars).

  night
      1, if observation was taken on day 1; 2, if observation was taken on
      day 2.

  Braun, W. J. (1995) An illustration of bootstrapping using video lottery
  terminal data. Journal of Statistics Education
  http://www.amstat.org/publications/jse/v3n2/datasets.braun.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vlt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 345 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vlt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/vlt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vlt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
