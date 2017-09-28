# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cu_summary(path):
  """Automobile Data from 'Consumer Reports' 1990

  The `cu.summary` data frame has 117 rows and 5 columns, giving data on
  makes of cars taken from the April, 1990 issue of *Consumer Reports*.

  This data frame contains the following columns:

  `Price`
      a numeric vector giving the list price in US dollars of a standard
      model

  `Country`
      of origin, a factor with levels Brazil, England, France, Germany,
      Japan, Japan/USA, Korea, Mexico, Sweden and USA

  `Reliability`
      an ordered factor with levels Much worse < worse < average < better
      < Much better

  `Mileage`
      fuel consumption miles per US gallon, as tested.

  `Type`
      a factor with levels `Compact` `Large` `Medium` `Small`
      `Sporty` `Van`

  *Consumer Reports*, April, 1990, pp. 235–288 quoted in

  John M. Chambers and Trevor J. Hastie eds. (1992) *Statistical Models in
  S*, Wadsworth and Brooks/Cole, Pacific Grove, CA, pp. 46–47.

  See Also
  ~~~~~~~~

  `car.test.frame`, `car90`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cu_summary.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 117 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cu_summary.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/rpart/cu.summary.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cu_summary.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
