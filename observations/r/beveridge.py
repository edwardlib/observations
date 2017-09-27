# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def beveridge(path):
  """beveridge

  Data loads lazily. Type data(beveridge) into the console.

  A data.frame with 135 rows and 8 variables:

  -  month. dec 200 through feb 2012

  -  urate. unemployment rate, percent

  -  vrate. vacancy rate, percent

  -  t. linear time trend

  -  urate\_1. L.urate

  -  vrate\_1. L.vrate

  -  curate. D.urate

  -  cvrate. D.vrate

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `beveridge.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 135 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'beveridge.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/beveridge.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='beveridge.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
