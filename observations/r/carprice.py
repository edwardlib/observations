# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def carprice(path):
  """US Car Price Data

  U.S. data extracted from `Cars93`, a data frame in the MASS package.

  This data frame contains the following columns:

  Type
      Type of car, e.g. Sporty, Van, Compact

  Min.Price
      Price for a basic model

  Price
      Price for a mid-range model

  Max.Price
      Price for a ‘premium’ model

  Range.Price
      Difference between Max.Price and Min.Price

  RoughRange
      Rough.Range plus some N(0,.0001) noise

  gpm100
      The number of gallons required to travel 100 miles

  MPG.city
      Average number of miles per gallon for city driving

  MPG.highway
      Average number of miles per gallon for highway driving

  MASS package

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `carprice.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'carprice.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/carprice.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='carprice.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
