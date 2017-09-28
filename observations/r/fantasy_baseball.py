# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fantasy_baseball(path):
  """FantasyBaseball

  Draft selection times for a fantasy baseball league

  A dataset with 24 observations on the following 9 variables.

  `Round`

  Round of the draft (1 to 24)

  `DJ`

  Draft time (in seconds) for D.J.

  `AR`

  Draft time (in seconds) for A.R.

  `BK`

  Draft time (in seconds) for B.K.

  `JW`

  Draft time (in seconds) for J.W.

  `TS`

  Draft time (in seconds) for T.S.

  `RL`

  Draft time (in seconds) for R.L.

  `DR`

  Draft time (in seconds) for D.R.

  `MF`

  Draft time (in seconds) for M.F.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fantasy_baseball.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fantasy_baseball.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FantasyBaseball.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fantasy_baseball.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
