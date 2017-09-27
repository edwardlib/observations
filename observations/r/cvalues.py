# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cvalues(path):
  """Historical speed of light measurements

  Measurements made beteween 1675 and 1972

  A data frame with 9 observations on the following 3 variables.

  `Year`
      Year of measurement

  `speed`
      estimated speed in meters per second

  `error`
      measurement error, as estimated by experimenter(s)

  http://en.wikipedia.org/wiki/Speed_of_light accessed 2011/12/22

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cvalues.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cvalues.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gamclass/cvalues.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cvalues.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
