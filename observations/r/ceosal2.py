# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ceosal2(path):
  """ceosal2

  Data loads lazily. Type data(ceosal2) into the console.

  A data.frame with 177 rows and 15 variables:

  -  salary. 1990 compensation, $1000s

  -  age. in years

  -  college. =1 if attended college

  -  grad. =1 if attended graduate school

  -  comten. years with company

  -  ceoten. years as ceo with company

  -  sales. 1990 firm sales, millions

  -  profits. 1990 profits, millions

  -  mktval. market value, end 1990, mills.

  -  lsalary. log(salary)

  -  lsales. log(sales)

  -  lmktval. log(mktval)

  -  comtensq. comten^2

  -  ceotensq. ceoten^2

  -  profmarg. profits as percent of sales

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ceosal2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 177 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ceosal2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/ceosal2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ceosal2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
