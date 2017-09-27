# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def minn38(path):
  """Minnesota High School Graduates of 1938

  The Minnesota high school graduates of 1938 were classified according to
  four factors, described below. The `minn38` data frame has 168 rows
  and 5 columns.

  This data frame contains the following columns:

  `hs`
      high school rank: `"L"`, `"M"` and `"U"` for lower, middle and
      upper third.

  `phs`
      post high school status: Enrolled in college, (`"C"`), enrolled in
      non-collegiate school, (`"N"`), employed full-time, (`"E"`) and
      other, (`"O"`).

  `fol`
      father's occupational level, (seven levels, `"F1"`, `"F2"`, ...,
      `"F7"`).

  `sex`
      sex: factor with levels\ `"F"` or `"M"`.

  `f`
      frequency.

  From R. L. Plackett, (1974) *The Analysis of Categorical Data.* London:
  Griffin

  who quotes the data from

  Hoyt, C. J., Krishnaiah, P. R. and Torrance, E. P. (1959) Analysis of

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `minn38.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 168 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'minn38.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/minn38.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='minn38.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
