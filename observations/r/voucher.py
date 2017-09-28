# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def voucher(path):
  """voucher

  Data loads lazily. Type data(voucher) into the console.

  A data.frame with 990 rows and 19 variables:

  -  studyid. student identifier

  -  black. = 1 if African-American

  -  hispanic. = 1 if Hispanic

  -  female. = 1 if female

  -  appyear. year of first application: 90 to 93

  -  mnce. math NCE test score, 1994

  -  select. = 1 if ever selected to attend choice school

  -  choice. = 1 if attending choice school, 1994

  -  selectyrs. years selected to attend choice school

  -  choiceyrs. years attended choice school

  -  mnce90. mnce in 1990

  -  selectyrs1. = 1 if selectyrs == 1

  -  selectyrs2. = 1 if selectyrs == 2

  -  selectyrs3. = 1 if selectyrs == 3

  -  selectyrs4. = 1 if selectyrs == 4

  -  choiceyrs1. = 1 if choiceyrs == 1

  -  choiceyrs2. = 1 if choiceyrs == 2

  -  choiceyrs3. = 1 if choiceyrs == 3

  -  choiceyrs4. = 1 if choiceyrs == 4

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `voucher.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 990 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'voucher.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/voucher.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='voucher.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
