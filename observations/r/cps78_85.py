# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cps78_85(path):
  """cps78\_85

  Data loads lazily. Type data(cps78\_85) into the console.

  A data.frame with 1084 rows and 15 variables:

  -  educ. years of schooling

  -  south. =1 if live in south

  -  nonwhite. =1 if nonwhite

  -  female. =1 if female

  -  married. =1 if married

  -  exper. age - educ - 6

  -  expersq. exper^2

  -  union. =1 if belong to union

  -  lwage. log hourly wage

  -  age. in years

  -  year. 78 or 85

  -  y85. =1 if year == 85

  -  y85fem. y85\*female

  -  y85educ. y85\*educ

  -  y85union. y85\*union

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cps78_85.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1084 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cps78_85.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/cps78_85.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cps78_85.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
