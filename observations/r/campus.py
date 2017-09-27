# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def campus(path):
  """campus

  Data loads lazily. Type data(campus) into the console.

  A data.frame with 97 rows and 7 variables:

  -  enroll. total enrollment

  -  priv. =1 if private college

  -  police. employed officers

  -  crime. total campus crimes

  -  lcrime. log(crime)

  -  lenroll. log(enroll)

  -  lpolice. log(police)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `campus.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 97 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'campus.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/campus.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='campus.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
