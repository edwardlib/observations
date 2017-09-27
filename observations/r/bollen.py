# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bollen(path):
  """Bollen's Data on Industrialization and Political Democracy

  This data set includes four measures of democracy at two points in time,
  1960 and 1965, and three measures of industrialization in 1960, for 75
  developing countries.

  A data frame with 75 observations on the following 11 variables.

  `y1`
      freedom of the press, 1960

  `y2`
      freedom of political opposition, 1960

  `y3`
      fairness of elections, 1960

  `y4`
      effectivness of elected legislature, 1960

  `y5`
      freedom of the press, 1965

  `y6`
      freedom of political opposition, 1965

  `y7`
      fairness of elections, 1965

  `y8`
      effectivness of elected legislature, 1965

  `x1`
      GNP per capita, 1960

  `x2`
      energy consumption per capita, 1960

  `x3`
      percentage of labor force in industry, 1960

  personal communication from Ken Bollen.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bollen.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 75 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bollen.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/sem/Bollen.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bollen.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
