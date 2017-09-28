# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wagner_growth(path):
  """Wagner's Hannover Employment Growth Data

  Wagner (1994) investigates the rate of employment growth (`y`) as
  function of percentage of people engaged in **p**\ roducation
  **a**\ ctivities (`PA`) and **h**\ igher **s**\ ervices (`HS`) and
  of the **g**\ rowth of these percentages (`GPA`, `GHS`) during three
  time periods in 21 geographical regions of the greater Hannover area.

  A data frame with *21 \* 3 = 63* observations (one per
  `Region x Period`) on the following 7 variables.

  `Region`
      a `factor` with 21 levels, denoting the corresponding region in
      Hannover (conceptually a “block factor”).

  `PA`
      numeric: percent of people involved in production activities.

  `GPA`
      **g**\ rowth of `PA`.

  `HS`
      a numeric vector

  `GHS`
      a numeric vector

  `y`
      a numeric vector

  `Period`
      a `factor` with levels `1:3`, denoting the time period, 1 =
      1979-1982, 2 = 1983-1988, 3 = 1989-1992.

  Hubert, M. and Rousseeuw, P. J. (1997). Robust regression with both
  continuous and binary regressors, *Journal of Statistical Planning and
  Inference* **57**, 153–163.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wagner_growth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 63 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wagner_growth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/wagnerGrowth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wagner_growth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
