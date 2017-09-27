# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def car_test_frame(path):
  """Automobile Data from 'Consumer Reports' 1990

  The `car.test.frame` data frame has 60 rows and 8 columns, giving data
  on makes of cars taken from the April, 1990 issue of *Consumer Reports*.
  This is part of a larger dataset, some columns of which are given in
  `cu.summary`.

  This data frame contains the following columns:

  `Price`
      a numeric vector giving the list price in US dollars of a standard
      model

  `Country`
      of origin, a factor with levels France, Germany, Japan , Japan/USA,
      Korea, Mexico, Sweden and USA

  `Reliability`
      a numeric vector coded `1` to `5`.

  `Mileage`
      fuel consumption miles per US gallon, as tested.

  `Type`
      a factor with levels `Compact` `Large` `Medium` `Small`
      `Sporty` `Van`

  `Weight`
      kerb weight in pounds.

  `Disp.`
      the engine capacity (displacement) in litres.

  `HP`
      the net horsepower of the vehicle.

  *Consumer Reports*, April, 1990, pp. 235–288 quoted in

  John M. Chambers and Trevor J. Hastie eds. (1992) *Statistical Models in
  S*, Wadsworth and Brooks/Cole, Pacific Grove, CA, pp. 46–47.

  See Also
  ~~~~~~~~

  `car90`, `cu.summary`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `car_test_frame.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'car_test_frame.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/rpart/car.test.frame.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='car_test_frame.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
