# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def alcohol1(path):
  """Alcohol Consumption per Capita

  These data provide per capita alcohol consumption values for many
  countries in 2005 and 2008. There are also a few countries for which
  there are data in other years.

  A data frame with 411 observations on the following variables.

  -  `country` country name

  -  `year` year

  -  `alcohol` per capita alcohol consumption

  Gapminder (http://www.gapminder.org/)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `alcohol1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 411 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'alcohol1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Alcohol.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='alcohol1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
