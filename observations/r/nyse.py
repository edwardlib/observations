# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nyse(path):
  """nyse

  Data loads lazily. Type data(nyse) into the console.

  A data.frame with 691 rows and 8 variables:

  -  price. NYSE stock price index

  -  return. 100\*(p - p(-1))/p(-1))

  -  return\_1. lagged return

  -  t.

  -  price\_1.

  -  price\_2.

  -  cprice. price - price\_1

  -  cprice\_1. lagged cprice

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nyse.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 691 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nyse.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/nyse.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nyse.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
