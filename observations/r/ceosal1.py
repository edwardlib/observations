# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ceosal1(path):
  """ceosal1

  Data loads lazily. Type data(ceosal1) into the console.

  A data.frame with 209 rows and 12 variables:

  -  salary. 1990 salary, thousands $

  -  pcsalary. percent change salary, 89-90

  -  sales. 1990 firm sales, millions $

  -  roe. return on equity, 88-90 avg

  -  pcroe. percent change roe, 88-90

  -  ros. return on firm's stock, 88-90

  -  indus. =1 if industrial firm

  -  finance. =1 if financial firm

  -  consprod. =1 if consumer product firm

  -  utility. =1 if transport. or utilties

  -  lsalary. natural log of salary

  -  lsales. natural log of sales

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ceosal1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 209 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ceosal1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/ceosal1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ceosal1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
