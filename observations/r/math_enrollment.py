# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def math_enrollment(path):
  """Math Enrollments

  Semester enrollments in mathematics courses

  A dataset with 11 observations on the following 3 variables.

  `Ayear`

  Academic year (for the fall)

  `Fall`

  Fall semester total enrollments

  `Spring`

  Spring semster total enrollments


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `math_enrollment.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'math_enrollment.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MathEnrollment.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='math_enrollment.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
