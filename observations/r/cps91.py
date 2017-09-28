# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cps91(path):
  """cps91

  Data loads lazily. Type data(cps91) into the console.

  A data.frame with 5634 rows and 24 variables:

  -  husage. husband's age

  -  husunion. =1 if hus. in union

  -  husearns. hus. weekly earns

  -  huseduc. husband's yrs schooling

  -  husblck. =1 if hus. black

  -  hushisp. =1 if hus. hispanic

  -  hushrs. hus. weekly hours

  -  kidge6. =1 if have child >= 6

  -  earns. wife's weekly earnings

  -  age. wife's age

  -  black. =1 if wife black

  -  educ. wife's yrs schooling

  -  hispanic. =1 if wife hispanic

  -  union. =1 if wife in union

  -  faminc. annual family income

  -  husexp. huseduc - husage - 6

  -  exper. age - educ - 6

  -  kidlt6. =1 if have child < 6

  -  hours. wife's weekly hours

  -  expersq. exper^2

  -  nwifeinc. non-wife inc, $1000s

  -  inlf. =1 if wife in labor force

  -  hrwage. earns/hours

  -  lwage. log(hrwage)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cps91.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5634 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cps91.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/cps91.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cps91.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
