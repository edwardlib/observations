# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def text_prices(path):
  """Text Prices

  Prices and number of pages for a sample of college textbooks

  A dataset with 30 observations on the following 2 variables.

  `Pages`

  Number of pages in the textbook

  `Price`

  Price of the textbook (in dollars)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `text_prices.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'text_prices.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/TextPrices.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='text_prices.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
