# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rdchem(path):
  """rdchem

  Data loads lazily. Type data(rdchem) into the console.

  A data.frame with 32 rows and 8 variables:

  -  rd. R&D spending, millions

  -  sales. firm sales, millions

  -  profits. profits, millions

  -  rdintens. rd as percent of sales

  -  profmarg. profits as percent of sales

  -  salessq. sales^2

  -  lsales. log(sales)

  -  lrd. log(rd)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rdchem.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rdchem.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/rdchem.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rdchem.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
