# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rwm(path):
  """rwm

  German health registry for the years 1984-1988. Health information for
  years prior to health reform.

  A data frame with 27,326 observations on the following 4 variables.

  `docvis`
      number of visits to doctor during year (0-121)

  `age`
      age: 25-64

  `educ`
      years of formal education (7-18)

  `hhninc`
      household yearly income in DM/1000)

  German Health Reform Registry, years pre-reform 1984-1988, From Hilbe
  and Greene (2008)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rwm.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27326 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rwm.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/rwm.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rwm.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
