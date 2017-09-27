# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mtcars(path):
  """Motor Trend Car Road Tests

  The data was extracted from the 1974 *Motor Trend* US magazine, and
  comprises fuel consumption and 10 aspects of automobile design and
  performance for 32 automobiles (1973–74 models).

  A data frame with 32 observations on 11 variables.

  +---------+--------+--------------------------------------------+
  | [, 1]   | mpg    | Miles/(US) gallon                          |
  +---------+--------+--------------------------------------------+
  | [, 2]   | cyl    | Number of cylinders                        |
  +---------+--------+--------------------------------------------+
  | [, 3]   | disp   | Displacement (cu.in.)                      |
  +---------+--------+--------------------------------------------+
  | [, 4]   | hp     | Gross horsepower                           |
  +---------+--------+--------------------------------------------+
  | [, 5]   | drat   | Rear axle ratio                            |
  +---------+--------+--------------------------------------------+
  | [, 6]   | wt     | Weight (1000 lbs)                          |
  +---------+--------+--------------------------------------------+
  | [, 7]   | qsec   | 1/4 mile time                              |
  +---------+--------+--------------------------------------------+
  | [, 8]   | vs     | V/S                                        |
  +---------+--------+--------------------------------------------+
  | [, 9]   | am     | Transmission (0 = automatic, 1 = manual)   |
  +---------+--------+--------------------------------------------+
  | [,10]   | gear   | Number of forward gears                    |
  +---------+--------+--------------------------------------------+
  | [,11]   | carb   | Number of carburetors                      |
  +---------+--------+--------------------------------------------+

  Henderson and Velleman (1981), Building multiple regression models
  interactively. *Biometrics*, **37**, 391–411.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mtcars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mtcars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/mtcars.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mtcars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
