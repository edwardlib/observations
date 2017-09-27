# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bwght(path):
  """bwght

  Data loads lazily. Type data(bwght) into the console.

  A data.frame with 1388 rows and 14 variables:

  -  faminc. 1988 family income, $1000s

  -  cigtax. cig. tax in home state, 1988

  -  cigprice. cig. price in home state, 1988

  -  bwght. birth weight, ounces

  -  fatheduc. father's yrs of educ

  -  motheduc. mother's yrs of educ

  -  parity. birth order of child

  -  male. =1 if male child

  -  white. =1 if white

  -  cigs. cigs smked per day while preg

  -  lbwght. log of bwght

  -  bwghtlbs. birth weight, pounds

  -  packs. packs smked per day while preg

  -  lfaminc. log(faminc)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bwght.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1388 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bwght.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/bwght.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bwght.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
