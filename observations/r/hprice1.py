# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hprice1(path):
  """hprice1

  Data loads lazily. Type data(hprice1) into the console.

  A data.frame with 88 rows and 10 variables:

  -  price. house price, $1000s

  -  assess. assessed value, $1000s

  -  bdrms. number of bdrms

  -  lotsize. size of lot in square feet

  -  sqrft. size of house in square feet

  -  colonial. =1 if home is colonial style

  -  lprice. log(price)

  -  lassess. log(assess

  -  llotsize. log(lotsize)

  -  lsqrft. log(sqrft)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hprice1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 88 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hprice1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/hprice1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hprice1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
