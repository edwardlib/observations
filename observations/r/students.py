# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def students(path):
  """Student Risk Taking

  Students were administered two parallel forms of a test after a random
  assignment to three different treatments.

  A data frame with 35 observations on the following 3 variables.

  `treatment`
      a factor with levels `AA`, `C`, and `NC`.

  `low`
      the result of the first test.

  `high`
      the result of the second test.

  N. H. Timm (2002), *Applied Multivariate Analysis*. Springer, New York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `students.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 35 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'students.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/students.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='students.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
