# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def perch(path):
  """Perch

  Size of perch caught in a Finnish lake

  A dataset with 56 observations on the following 4 variables.

  `Obs`

  Observation number

  `Weight`

  Weight (in grams)

  `Length`

  Length (in centimeters)

  `Width`

  Width (in centimeters

  JSE Data Archive,
  http://www.amstat.org/publications/jse/jse\_data\_archive.htm, submitted

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `perch.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'perch.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Perch.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='perch.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
