# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sleep(path):
  """Student's Sleep Data

  Data which show the effect of two soporific drugs (increase in hours of
  sleep compared to control) on 10 patients.

  A data frame with 20 observations on 3 variables.

  +---------+---------+-----------+------------------------------+
  | [, 1]   | extra   | numeric   | increase in hours of sleep   |
  +---------+---------+-----------+------------------------------+
  | [, 2]   | group   | factor    | drug given                   |
  +---------+---------+-----------+------------------------------+
  | [, 3]   | ID      | factor    | patient ID                   |
  +---------+---------+-----------+------------------------------+

  Cushny, A. R. and Peebles, A. R. (1905) The action of optical isomers:
  II hyoscines. *The Journal of Physiology* **32**, 501–510.

  Student (1908) The probable error of the mean. *Biometrika*, **6**, 20.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sleep.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sleep.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/sleep.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sleep.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
