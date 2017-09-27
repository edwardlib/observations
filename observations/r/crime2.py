# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crime2(path):
  """crime2

  Data loads lazily. Type data(crime2) into the console.

  A data.frame with 92 rows and 34 variables:

  -  pop. population

  -  crimes. total number index crimes

  -  unem. unemployment rate

  -  officers. number police officers

  -  pcinc. per capita income

  -  west. =1 if city in west

  -  nrtheast. =1 if city in NE

  -  south. =1 if city in south

  -  year. 82 or 87

  -  area. land area, square miles

  -  d87. =1 if year = 87

  -  popden. people per sq mile

  -  crmrte. crimes per 1000 people

  -  offarea. officers per sq mile

  -  lawexpc. law enforce. expend. pc, $

  -  polpc. police per 1000 people

  -  lpop. log(pop)

  -  loffic. log(officers)

  -  lpcinc. log(pcinc)

  -  llawexpc. log(lawexpc)

  -  lpopden. log(popden)

  -  lcrimes. log(crimes)

  -  larea. log(area)

  -  lcrmrte. log(crmrte)

  -  clcrimes. change in lcrimes

  -  clpop. change in lpop

  -  clcrmrte. change in lcrmrte

  -  lpolpc. log(polpc)

  -  clpolpc. change in lpolpc

  -  cllawexp. change in llawexp

  -  cunem. change in unem

  -  clpopden. change in lpopden

  -  lcrmrt\_1. lcrmrte lagged

  -  ccrmrte. change in crmrte

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crime2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 92 rows and 34 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crime2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/crime2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crime2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
