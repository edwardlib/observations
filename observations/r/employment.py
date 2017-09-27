# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def employment(path):
  """Employment Status

  Data from a 1974 Danish study given by Andersen (1991) on the employees
  who had been laid off. The workers are classified by their employment
  status on 1975-01-01, the cause of their layoff and the length of
  employment before they were laid off.

  A 3-dimensional array resulting from cross-tabulating variables for 1314
  employees. The variables and their levels are as follows:

  +------+--------------------+-------------------------------------------+
  | No   | Name               | Levels                                    |
  +------+--------------------+-------------------------------------------+
  | 1    | EmploymentStatus   | NewJob, Unemployed                        |
  +------+--------------------+-------------------------------------------+
  | 2    | EmploymentLength   | <1Mo, 1-3Mo, 3-12Mo, 1-2Yr, 2-5Yr, >5Yr   |
  +------+--------------------+-------------------------------------------+
  | 3    | LayoffCause        | Closure, Replaced                         |
  +------+--------------------+-------------------------------------------+

  Michael Friendly (2000), Visualizing Categorical Data, pages 126–129.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `employment.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'employment.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Employment.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='employment.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
