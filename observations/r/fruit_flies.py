# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fruit_flies(path):
  """FruitFlies

  Sexual activity and lifetimes of fruit flies

  A dataset with 125 observations on the following 7 variables.

  `ID`

  a numeric vector

  `Partners`

  Number of female partners: 0, 1, or 8

  `Type`

  `0`\ =pregnant, `1`\ =virgin, `9`\ =none

  `Longevity`

  Lifespan (in days)

  `Thorax`

  Length of thorax (in mm)

  `Sleep`

  Percent of day sleeping

  `Treatment`

  `1 pregnant`, `1 virgin`, `8 pregnant`, `8 virgin`, or `none`

  The data are given as part of the data archive on the Journal of
  Statistics Education website and can be found on the page
  http://www.amstat.org/publications/jse/jse\_data\_archive.htm.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fruit_flies.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 125 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fruit_flies.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FruitFlies.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fruit_flies.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
