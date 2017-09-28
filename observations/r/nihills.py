# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nihills(path):
  """Record times for Northern Ireland mountain running events

  Data were from the 2007 calendar for the Northern Ireland Mountain
  Running Association.

  A data frame with 23 observations on the following 4 variables.

  `dist`
      distances in miles

  `climb`
      amount of climb in feet

  `time`
      record time in hours for males

  `timef`
      record time in hours for females

  For more recent information, see
  http://www.nimra.org.uk/index.php/fixtures/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nihills.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nihills.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/nihills.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nihills.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
