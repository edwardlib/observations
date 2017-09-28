# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pedometer(path):
  """Pedometer

  Daily walking amounts recorded on a personal pedometer from
  September-December 2011

  A dataset with 68 observations on the following 8 variables.

  `Steps`

  Total number of steps for the day

  `Moderate`

  Number of steps at a moderate walking speed

  `Min`

  Number of minutes walking at a moderate speed

  `kcal`

  Number of calories burned walking at a moderate speed

  `Mile`

  Total number of miles walked

  `Rain`

  Type of weather (`rain` or `shine`)

  `Day`

  Day of the week (`U`\ =Sunday, `M`\ =Monday, `T`\ =Tuesday,
  `W`\ =Wednesday, `R`\ =Thursday, `F`\ =Friday, `S`\ =Saturday

  `DayType`

  Coded as `Weekday` or `Weekend`


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pedometer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 68 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pedometer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Pedometer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pedometer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
