# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def discrim(path):
  """discrim

  Data loads lazily. Type data(discrim) into the console.

  A data.frame with 410 rows and 37 variables:

  -  psoda. price of medium soda, 1st wave

  -  pfries. price of small fries, 1st wave

  -  pentree. price entree (burger or chicken), 1st wave

  -  wagest. starting wage, 1st wave

  -  nmgrs. number of managers, 1st wave

  -  nregs. number of registers, 1st wave

  -  hrsopen. hours open, 1st wave

  -  emp. number of employees, 1st wave

  -  psoda2. price of medium soday, 2nd wave

  -  pfries2. price of small fries, 2nd wave

  -  pentree2. price entree, 2nd wave

  -  wagest2. starting wage, 2nd wave

  -  nmgrs2. number of managers, 2nd wave

  -  nregs2. number of registers, 2nd wave

  -  hrsopen2. hours open, 2nd wave

  -  emp2. number of employees, 2nd wave

  -  compown. =1 if company owned

  -  chain. BK = 1, KFC = 2, Roy Rogers = 3, Wendy's = 4

  -  density. population density, town

  -  crmrte. crime rate, town

  -  state. NJ = 1, PA = 2

  -  prpblck. proportion black, zipcode

  -  prppov. proportion in poverty, zipcode

  -  prpncar. proportion no car, zipcode

  -  hseval. median housing value, zipcode

  -  nstores. number of stores, zipcode

  -  income. median family income, zipcode

  -  county. county label

  -  lpsoda. log(psoda)

  -  lpfries. log(pfries)

  -  lhseval. log(hseval)

  -  lincome. log(income)

  -  ldensity. log(density)

  -  NJ. =1 for New Jersey

  -  BK. =1 if Burger King

  -  KFC. =1 if Kentucky Fried Chicken

  -  RR. =1 if Roy Rogers

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `discrim.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 410 rows and 37 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'discrim.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/discrim.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='discrim.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
