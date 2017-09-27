# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def marathon(path):
  """Marathon

  Training records for a marathon runner

  A dataset with 1128 observations on the following 9 variables.

  `Date`

  Training date

  `Miles`

  Miles for training run

  `Time`

  Training time (in minutes:seconds:hundredths)

  `Pace`

  Running pace (in minutes:seconds:hundredths per mile)

  `ShoeBrand`

  `Addidas`, `Asics`, `Brooks`, `Izumi`, `Mizuno`, or
  `New Balance`

  `TimeMin`

  Training time (in minutes)

  `PaceMin`

  Running pace (in minutes per mile)

  `Short`

  `1`\ = 5 miles or less or `0`\ =more than 5 miles

  `After2004`

  `1`\ = for runs after 2004 or `0`\ =for earlier runs


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `marathon.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1127 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'marathon.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Marathon.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='marathon.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
