# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ten_mile_race(path):
  """Cherry Blossom Race

  The Cherry Blossom 10 Mile Run is a road race held in Washington, D.C.
  in April each year. (The name comes from the famous cherry trees that
  are in bloom in April in Washington.) The results of this race are
  published. This data frame contains the results from the 2005 race.

  A data frame with 8636 observations on the following variables.

  -  `state` State of residence of runner.

  -  `time` Official time from starting gun to finish line.

  -  `net` The recorded time (in seconds) from when the runner crossed
     the starting line to when the runner crossed the finish line. This is
     generally less than the official time because of the large number of
     runners in the race: it takes time to reach the starting line after
     the gun has gone off.

  -  `age` Age of runner in years.

  -  `sex` A factor with levels `F` `M`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ten_mile_race.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8636 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ten_mile_race.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/TenMileRace.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ten_mile_race.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
