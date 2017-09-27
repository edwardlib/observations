# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def prostitutes(path):
  """Parent-Duchatelet's time-series data on the number of prostitutes in Paris

  A table indicating month by month, for the years 1812-1854, the number
  of prostitutes on the registers of the administration of the city of
  Paris.

  A data frame with 516 observations on the following 5 variables.

  `Year`
      a numeric vector

  `month`
      a factor with levels `Apr` `Aug` `Dec` `Feb` `Jan` `Jul`
      `Jun` `Mar` `May` `Nov` `Oct` `Sep`

  `count`
      a numeric vector: number of prostitutes

  `mon`
      a numeric vector: numeric month

  `date`
      a Date

  Parent-Duchatelet, A. (1857), *De la prostitution dans la ville de
  Paris*, 3rd ed, p. 32, 36

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `prostitutes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 516 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'prostitutes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Prostitutes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='prostitutes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
