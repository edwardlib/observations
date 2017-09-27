# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pulse(path):
  """Pulse

  Pulse rates before and after exercise for a sample of statistics
  students

  A dataset with 232 observations on the following 7 variables.

  `Active`

  Pulse rate (beats per minute) after exercise

  `Rest`

  Resting pulse rate (beats per minute)

  `Smoke`

  `1`\ =smoker or `0`\ =nonsmoker

  `Gender`

  `1`\ =female or `0`\ =male

  `Exercise`

  Typical hours of exercise (per week)

  `Hgt`

  Height (in inches)

  `Wgt`

  Weight (in pounds)

  Data compiled over several semesters from students taking a Stat2

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pulse.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 232 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pulse.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Pulse.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pulse.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
