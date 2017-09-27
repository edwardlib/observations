# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def overdrawn(path):
  """Overdrawn

  Overdrawn

  A dataset with 450 observations on the following 4 variables.

  `Age`

  Age of the student (in years)

  `Sex`

  `0`\ =male or `1`\ =female

  `DaysDrink`

  Number of days drinking alcohol (in past 30 days)

  `Overdrawn`

  Has student overdrawn a checking account? `0`\ =no or `1`\ =yes

  Worthy S.L., Jonkman J.N., Blinn-Pike L. (2010), "Sensation-Seeking,
  Risk-Taking, and Problematic Financial Behaviors of College Students,"

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `overdrawn.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 450 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'overdrawn.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Overdrawn.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='overdrawn.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
