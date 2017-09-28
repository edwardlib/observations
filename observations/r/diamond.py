# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def diamond(path):
  """Pricing the C's of Diamond Stones

  a cross-section from 2000

  *number of observations* : 308

  *observation* : goods

  *country* : Singapore

  A dataframe containing :

  carat
      weight of diamond stones in carat unit

  colour
      a factor with levels (D,E,F,G,H,I)

  clarity
      a factor with levels (IF,VVS1,VVS2,VS1,VS2)

  certification
      certification body, a factor with levels (GIA,IGI,HRD)

  price
      price in Singapore \\$

  Chu, Singfat (2001) “Pricing the C's of Diamond Stones”, *Journal of
  Statistics Education*, **9(2)**.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `diamond.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 308 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'diamond.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Diamond.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='diamond.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
