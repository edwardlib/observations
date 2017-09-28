# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def birthdays(path):
  """US Births in 1969 - 1988

  A day by day record of the number of births in each US State.

  A data frame with 374221 observations on the following variables.

  -  `state` state where child was born

  -  `year` year (1969-1988)

  -  `month` month (1-12)

  -  `day` day of month

  -  `date` date as a date object

  -  `births` number of births

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `birthdays.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 372864 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'birthdays.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Birthdays.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='birthdays.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
