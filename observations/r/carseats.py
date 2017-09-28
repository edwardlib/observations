# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def carseats(path):
  """Sales of Child Car Seats

  A simulated data set containing sales of child car seats at 400
  different stores.

  A data frame with 400 observations on the following 11 variables.

  `Sales`
      Unit sales (in thousands) at each location

  `CompPrice`
      Price charged by competitor at each location

  `Income`
      Community income level (in thousands of dollars)

  `Advertising`
      Local advertising budget for company at each location (in thousands
      of dollars)

  `Population`
      Population size in region (in thousands)

  `Price`
      Price company charges for car seats at each site

  `ShelveLoc`
      A factor with levels `Bad`, `Good` and `Medium` indicating the
      quality of the shelving location for the car seats at each site

  `Age`
      Average age of the local population

  `Education`
      Education level at each location

  `Urban`
      A factor with levels `No` and `Yes` to indicate whether the
      store is in an urban or rural location

  `US`
      A factor with levels `No` and `Yes` to indicate whether the
      store is in the US or not

  Simulated data

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `carseats.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 400 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'carseats.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Carseats.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='carseats.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
