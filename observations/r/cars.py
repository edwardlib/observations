# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cars(path):
  """Speed and Stopping Distances of Cars

  The data give the speed of cars and the distances taken to stop. Note
  that the data were recorded in the 1920s.

  A data frame with 50 observations on 2 variables.

  +--------+---------+-----------+--------------------------+
  | [,1]   | speed   | numeric   | Speed (mph)              |
  +--------+---------+-----------+--------------------------+
  | [,2]   | dist    | numeric   | Stopping distance (ft)   |
  +--------+---------+-----------+--------------------------+

  Ezekiel, M. (1930) *Methods of Correlation Analysis*. Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/cars.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
