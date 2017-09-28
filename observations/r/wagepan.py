# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wagepan(path):
  """wagepan

  Data loads lazily. Type data(wagepan) into the console.

  A data.frame with 4360 rows and 44 variables:

  -  nr. person identifier

  -  year. 1980 to 1987

  -  agric. =1 if in agriculture

  -  black. =1 if black

  -  bus.

  -  construc. =1 if in construction

  -  ent.

  -  exper. labor mkt experience

  -  fin.

  -  hisp. =1 if Hispanic

  -  poorhlth. =1 if in poor health

  -  hours. annual hours worked

  -  manuf. =1 if in manufacturing

  -  married. =1 if married

  -  min.

  -  nrthcen. =1 if north central

  -  nrtheast. =1 if north east

  -  occ1.

  -  occ2.

  -  occ3.

  -  occ4.

  -  occ5.

  -  occ6.

  -  occ7.

  -  occ8.

  -  occ9.

  -  per.

  -  pro.

  -  pub.

  -  rur.

  -  south. =1 if south

  -  educ. years of schooling

  -  tra.

  -  trad.

  -  union. =1 if in union

  -  lwage. log(wage)

  -  d81. =1 if year == 1981

  -  d82.

  -  d83.

  -  d84.

  -  d85.

  -  d86.

  -  d87.

  -  expersq. exper^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wagepan.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4360 rows and 44 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wagepan.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/wagepan.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wagepan.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
