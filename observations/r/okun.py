# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def okun(path):
  """okun

  Data loads lazily. Type data(okun) into the console.

  A data.frame with 47 rows and 4 variables:

  -  year. 1959 through 2005

  -  pcrgdp. percentage change in real GDP

  -  unem. civilian unemployment rate

  -  cunem. unem - unem[\_n-1]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `okun.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 47 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'okun.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/okun.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='okun.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
