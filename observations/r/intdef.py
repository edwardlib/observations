# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def intdef(path):
  """intdef

  Data loads lazily. Type data(intdef) into the console.

  A data.frame with 56 rows and 13 variables:

  -  year. 1948 to 2003

  -  i3. 3 month T-bill rate

  -  inf. CPI inflation rate

  -  rec. federal receipts, percent GDP

  -  out. federal outlays, percent GDP

  -  def. out - rec

  -  i3\_1. i3[\_n-1]

  -  inf\_1. inf[\_n-1]

  -  def\_1. def[\_n-1]

  -  ci3. i3 - i3\_1

  -  cinf. inf - inf\_1

  -  cdef. def - def\_1

  -  y77. =1 if year >= 1977; change in FY

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `intdef.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 56 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'intdef.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/intdef.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='intdef.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
