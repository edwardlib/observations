# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def labor_supply(path):
  """Wages and Hours Worked

  a panel of 532 observations from 1979 to 1988

  *number of observations* : 5320

  A dataframe containing :

  lnhr
      log of annual hours worked

  lnwg
      log of hourly wage

  kids
      number of children

  age
      age

  disab
      bad health

  id
      id

  year
      year

  Ziliak, Jim (1997) “Efficient Estimation With Panel Data when
  Instruments are Predetermined: An Empirical Comparison of
  Moment-Condition Estimators”, *Journal of Business and Economic
  Statistics*, **419–431**.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `labor_supply.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5320 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'labor_supply.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/LaborSupply.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='labor_supply.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
