# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sleepstudy(path):
  """Reaction times in a sleep deprivation study

  The average reaction time per day for subjects in a sleep deprivation
  study. On day 0 the subjects had their normal amount of sleep. Starting
  that night they were restricted to 3 hours of sleep per night. The
  observations represent the average reaction time on a series of tests
  given each day to each subject.

  A data frame with 180 observations on the following 3 variables.

  `Reaction`
      Average reaction time (ms)

  `Days`
      Number of days of sleep deprivation

  `Subject`
      Subject number on which the observation was made.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sleepstudy.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 180 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sleepstudy.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lme4/sleepstudy.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sleepstudy.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
