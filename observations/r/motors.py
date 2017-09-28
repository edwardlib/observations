# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def motors(path):
  """Accelerated Life Testing of Motorettes

  The `motors` data frame has 40 rows and 3 columns. It describes an
  accelerated life test at each of four temperatures of 10 motorettes, and
  has rather discrete times.

  This data frame contains the following columns:

  `temp`
      the temperature (degrees C) of the test.

  `time`
      the time in hours to failure or censoring at 8064 hours (= 336
      days).

  `cens`
      an indicator variable for death.

  Kalbfleisch, J. D. and Prentice, R. L. (1980) *The Statistical Analysis
  of Failure Time Data.* New York: Wiley.

  taken from

  Nelson, W. D. and Hahn, G. J. (1972) Linear regression of a regression
  relationship from censored data. Part 1 – simple methods and their
  application. *Technometrics*, **14**, 247–276.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `motors.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'motors.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/motors.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='motors.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
