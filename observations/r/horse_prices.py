# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def horse_prices(path):
  """HorsePrices

  HorsePrices

  A dataset with 50 observations on the following 5 variables.

  `HorseID`

  ID code for each horse

  `Price`

  Price (in dollars)

  `Age`

  Age of the horse (in years)

  `Height`

  Height fo the horse (in hands)

  `Sex`

  `f`\ =female `m`\ =male


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `horse_prices.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'horse_prices.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/HorsePrices.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='horse_prices.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
