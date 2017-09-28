# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def apple(path):
  """apple

  Data loads lazily. Type data(apple) into the console.

  A data.frame with 660 rows and 17 variables:

  -  id. respondent identifier

  -  educ. years schooling

  -  date. date: month/day/year

  -  state. home state

  -  regprc. price of regular apples

  -  ecoprc. price of ecolabeled apples

  -  inseason. =1 if interviewed in Nov.

  -  hhsize. household size

  -  male. =1 if male

  -  faminc. family income, thousands

  -  age. in years

  -  reglbs. quantity regular apples, pounds

  -  ecolbs. quantity ecolabeled apples, lbs

  -  numlt5. # in household younger than 5

  -  num5\_17. # in household 5 to 17

  -  num18\_64. # in household 18 to 64

  -  numgt64. # in household older than 64

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `apple.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 660 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'apple.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/apple.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='apple.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
