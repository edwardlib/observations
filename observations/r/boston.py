# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def boston(path):
  """Housing Values in Suburbs of Boston

  The `Boston` data frame has 506 rows and 14 columns.

  This data frame contains the following columns:

  `crim`
      per capita crime rate by town.

  `zn`
      proportion of residential land zoned for lots over 25,000 sq.ft.

  `indus`
      proportion of non-retail business acres per town.

  `chas`
      Charles River dummy variable (= 1 if tract bounds river; 0
      otherwise).

  `nox`
      nitrogen oxides concentration (parts per 10 million).

  `rm`
      average number of rooms per dwelling.

  `age`
      proportion of owner-occupied units built prior to 1940.

  `dis`
      weighted mean of distances to five Boston employment centres.

  `rad`
      index of accessibility to radial highways.

  `tax`
      full-value property-tax rate per \\$10,000.

  `ptratio`
      pupil-teacher ratio by town.

  `black`
      *1000(Bk - 0.63)^2* where *Bk* is the proportion of blacks by town.

  `lstat`
      lower status of the population (percent).

  `medv`
      median value of owner-occupied homes in \\$1000s.

  Harrison, D. and Rubinfeld, D.L. (1978) Hedonic prices and the demand
  for clean air. *J. Environ. Economics and Management* **5**, 81–102.

  Belsley D.A., Kuh, E. and Welsch, R.E. (1980) *Regression Diagnostics.
  Identifying Influential Data and Sources of Collinearity.* New York:

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `boston.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 506 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'boston.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Boston.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='boston.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
