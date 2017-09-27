# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mroz2(path):
  """mroz

  Data loads lazily. Type data(mroz) into the console.

  A data.frame with 753 rows and 22 variables:

  -  inlf. =1 if in lab frce, 1975

  -  hours. hours worked, 1975

  -  kidslt6. # kids < 6 years

  -  kidsge6. # kids 6-18

  -  age. woman's age in yrs

  -  educ. years of schooling

  -  wage. est. wage from earn, hrs

  -  repwage. rep. wage at interview in 1976

  -  hushrs. hours worked by husband, 1975

  -  husage. husband's age

  -  huseduc. husband's years of schooling

  -  huswage. husband's hourly wage, 1975

  -  faminc. family income, 1975

  -  mtr. fed. marg. tax rte facing woman

  -  motheduc. mother's years of schooling

  -  fatheduc. father's years of schooling

  -  unem. unem. rate in county of resid.

  -  city. =1 if live in SMSA

  -  exper. actual labor mkt exper

  -  nwifeinc. (faminc - wage\*hours)/1000

  -  lwage. log(wage)

  -  expersq. exper^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mroz2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 753 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mroz2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/mroz.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mroz2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
