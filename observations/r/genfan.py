# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def genfan(path):
  """Generator fans

  The data come from a field engineering study of the time to failure of
  diesel generator fans. The ultimate goal was to decide whether or not to
  replace the working fans with a higher quality fan to prevent future
  failures. Seventy generators were studied. For each one, the number of
  hours of running time from its first being put into service until fan
  failure or until the end of the study(whichever came first) was
  recorded.

  A data frame with 70 observations on the following 2 variables.

  `hours`
      hours of service

  `status`
      1=failure, 0=censored

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `genfan.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 70 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'genfan.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/genfan.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='genfan.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
