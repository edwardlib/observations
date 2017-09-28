# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rdtelec(path):
  """rdtelec

  Data loads lazily. Type data(rdtelec) into the console.

  A data.frame with 29 rows and 6 variables:

  -  rd. R&D spending, millions $

  -  sales. firm sales, millions $

  -  rdintens. rd as percent of sales

  -  lrd. log(rd)

  -  lsales. log(sales)

  -  salessq. sales^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rdtelec.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 29 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rdtelec.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/rdtelec.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rdtelec.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
