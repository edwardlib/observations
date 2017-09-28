# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def three_cars(path):
  """Three Cars

  Compare prices for Porsche, Jaguar, and BMW cars offered for sale at an
  internet site

  A dataset with 90 observations on the following 8 variables.

  `CarType`

  `BMW`, `Jaguar`, or `Porsche`

  `Price`

  Asking price (in $1,000's)

  `Age`

  Age of the car (in years)

  `Mileage`

  previous miles driven (in 1,000's)

  `Car`

  `0`\ =Porsche, `1`\ =Jaguar, `2`\ =BMW

  `Porsche`

  Indicator with `1`\ = Porsche and `0`\ =otherwise

  `Jaguar`

  Indicator with `1`\ = Jaguar and `0`\ =otherwise

  `BMW`

  Indicator with `1`\ = BMW and `0`\ =otherwise


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `three_cars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'three_cars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/ThreeCars.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='three_cars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
