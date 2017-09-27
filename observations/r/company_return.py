# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def company_return(path):
  """return

  Data loads lazily. Type data(return) into the console.

  A data.frame with 142 rows and 12 variables:

  -  roe. return on equity, 1990

  -  rok. return on capital, 1990

  -  dkr. debt/capital, 1990

  -  eps. earnings per share, 1990

  -  netinc. net income, 1990 (mills.)

  -  sp90. stock price, end 1990

  -  sp94. stock price, end 1994

  -  salary. CEO salary, 1990 (thous.)

  -  return. percent change s.p., 90-94

  -  lsalary. log(salary)

  -  lsp90. log(sp90)

  -  lnetinc. log(netinc)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `company_return.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 142 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'company_return.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/return.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='company_return.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
