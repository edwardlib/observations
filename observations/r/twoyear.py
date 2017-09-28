# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def twoyear(path):
  """twoyear

  Data loads lazily. Type data(twoyear) into the console.

  A data.frame with 6763 rows and 23 variables:

  -  female. =1 if female

  -  phsrank. percent high school rank; 100 = best

  -  BA. =1 if Bachelor's degree

  -  AA. =1 if Associate's degree

  -  black. =1 if African-American

  -  hispanic. =1 if Hispanic

  -  id. ID Number

  -  exper. total (actual) work experience

  -  jc. total 2-year credits

  -  univ. total 4-year credits

  -  lwage. log hourly wage

  -  stotal. total standardized test score

  -  smcity. =1 if small city, 1972

  -  medcity. =1 if med. city, 1972

  -  submed. =1 if suburb med. city, 1972

  -  lgcity. =1 if large city, 1972

  -  sublg. =1 if suburb large city, 1972

  -  vlgcity. =1 if very large city, 1972

  -  subvlg. =1 if sub. very lge. city, 1972

  -  ne. =1 if northeast

  -  nc. =1 if north central

  -  south. =1 if south

  -  totcoll. jc + univ

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `twoyear.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6763 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'twoyear.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/twoyear.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='twoyear.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
