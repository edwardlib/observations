# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def schooldays(path):
  """Days not Spent at School

  Data from a sociological study, the number of days absent from school is
  the response variable.

  A data frame with 154 observations on the following 5 variables.

  `race`
      race of the child, a factor with levels `aboriginal` and
      `non-aboriginal`.

  `sex`
      the sex of the child, a factor with levels `female` and `male`.

  `school`
      the school type, a factor with levels `F0` (primary), `F1`
      (first), `F2` (second) and `F3` (third form).

  `learner`
      how good is the child in learning things, a factor with levels
      `average` and `slow`.

  `absent`
      number of days absent from school.

  S. Quine (1975), Achievement Orientation of Aboriginal and White
  Adolescents. Doctoral Dissertation, Australian National University,
  Canberra.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `schooldays.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 154 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'schooldays.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/schooldays.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='schooldays.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
