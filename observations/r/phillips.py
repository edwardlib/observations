# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def phillips(path):
  """phillips

  Data loads lazily. Type data(phillips) into the console.

  A data.frame with 56 rows and 7 variables:

  -  year. 1948 through 2003

  -  unem. civilian unemployment rate, percent

  -  inf. percentage change in CPI

  -  inf\_1. inf[\_n-1]

  -  unem\_1. unem[\_n-1]

  -  cinf. inf - inf\_1

  -  cunem. unem - unem\_1

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `phillips.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'phillips.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/phillips.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='phillips.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
