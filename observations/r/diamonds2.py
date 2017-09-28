# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def diamonds2(path):
  """Diamonds2

  A subset of the Diamonds data

  A dataset with 307 observations on the following 6 variables.

  `Carat`

  Size of the diamond (in carats)

  `Color`

  Coded as `D`\ (most white/bright) through `G`

  `Clarity`

  Coded as `IF`, `VVS1`, `VVS2`, `VS1`, `VS2`, `SI1`, `SI2`,
  or `SI3`

  `Depth`

  Depth (as a percentage of diameter)

  `PricePerCt`

  Price per carat

  `TotalPrice`

  Price for the diamond (in dollars)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `diamonds2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 307 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'diamonds2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Diamonds2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='diamonds2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
