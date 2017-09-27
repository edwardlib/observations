# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def auto(path):
  """Auto Data Set

  Gas mileage, horsepower, and other information for 392 vehicles.

  A data frame with 392 observations on the following 9 variables.

  `mpg`
      miles per gallon

  `cylinders`
      Number of cylinders between 4 and 8

  `displacement`
      Engine displacement (cu. inches)

  `horsepower`
      Engine horsepower

  `weight`
      Vehicle weight (lbs.)

  `acceleration`
      Time to accelerate from 0 to 60 mph (sec.)

  `year`
      Model year (modulo 100)

  `origin`
      Origin of car (1. American, 2. European, 3. Japanese)

  `name`
      Vehicle name

  The orginal data contained 408 observations but 16 observations with
  missing values were removed.

  This dataset was taken from the StatLib library which is maintained at
  Carnegie Mellon University. The dataset was used in the 1983 American
  Statistical Association Exposition.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `auto.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 392 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'auto.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Auto.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='auto.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
