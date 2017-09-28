# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_arrests(path):
  """Violent Crime Rates by US State

  This data set contains statistics, in arrests per 100,000 residents for
  assault, murder, and rape in each of the 50 US states in 1973. Also
  given is the percent of the population living in urban areas.

  A data frame with 50 observations on 4 variables.

  +--------+------------+-----------+---------------------------------+
  | [,1]   | Murder     | numeric   | Murder arrests (per 100,000)    |
  +--------+------------+-----------+---------------------------------+
  | [,2]   | Assault    | numeric   | Assault arrests (per 100,000)   |
  +--------+------------+-----------+---------------------------------+
  | [,3]   | UrbanPop   | numeric   | Percent urban population        |
  +--------+------------+-----------+---------------------------------+
  | [,4]   | Rape       | numeric   | Rape arrests (per 100,000)      |
  +--------+------------+-----------+---------------------------------+

  World Almanac and Book of facts 1975. (Crime rates).

  Statistical Abstracts of the United States 1975. (Urban rates).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_arrests.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_arrests.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/USArrests.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_arrests.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
