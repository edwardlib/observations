# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def athlet1(path):
  """athlet1

  Data loads lazily. Type data(athlet1) into the console.

  A data.frame with 118 rows and 23 variables:

  -  year. 1992 or 1993

  -  apps. # applics for admission

  -  top25. perc frsh class in 25 hs perc

  -  ver500. perc frsh >= 500 on verbal SAT

  -  mth500. perc frsh >= 500 on math SAT

  -  stufac. student-faculty ratio

  -  bowl. = 1 if bowl game in prev yr

  -  btitle. = 1 if men's cnf chmps prv yr

  -  finfour. = 1 if men's final 4 prv yr

  -  lapps. log(apps)

  -  d93. =1 if year = 1993

  -  avg500. (ver500+mth500)/2

  -  cfinfour. change in finfour

  -  clapps. change in lapps

  -  cstufac. change in stufac

  -  cbowl. change in bowl

  -  cavg500. change in avg500

  -  cbtitle. change in btitle

  -  lapps\_1. lapps lagged

  -  school. name of university

  -  ctop25. change in top25

  -  bball. =1 if btitle or finfour

  -  cbball. change in bball

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `athlet1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 118 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'athlet1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/athlet1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='athlet1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
