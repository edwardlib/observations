# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def card(path):
  """card

  Data loads lazily. Type data(card) into the console.

  A data.frame with 3010 rows and 34 variables:

  -  id. person identifier

  -  nearc2. =1 if near 2 yr college, 1966

  -  nearc4. =1 if near 4 yr college, 1966

  -  educ. years of schooling, 1976

  -  age. in years

  -  fatheduc. father's schooling

  -  motheduc. mother's schooling

  -  weight. NLS sampling weight, 1976

  -  momdad14. =1 if live with mom, dad at 14

  -  sinmom14. =1 if with single mom at 14

  -  step14. =1 if with step parent at 14

  -  reg661. =1 for region 1, 1966

  -  reg662. =1 for region 2, 1966

  -  reg663. =1 for region 3, 1966

  -  reg664. =1 for region 4, 1966

  -  reg665. =1 for region 5, 1966

  -  reg666. =1 for region 6, 1966

  -  reg667. =1 for region 7, 1966

  -  reg668. =1 for region 8, 1966

  -  reg669. =1 for region 9, 1966

  -  south66. =1 if in south in 1966

  -  black. =1 if black

  -  smsa. =1 in in SMSA, 1976

  -  south. =1 if in south, 1976

  -  smsa66. =1 if in SMSA, 1966

  -  wage. hourly wage in cents, 1976

  -  enroll. =1 if enrolled in school, 1976

  -  KWW. knowledge world of work score

  -  IQ. IQ score

  -  married. =1 if married, 1976

  -  libcrd14. =1 if lib. card in home at 14

  -  exper. age - educ - 6

  -  lwage. log(wage)

  -  expersq. exper^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `card.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3010 rows and 34 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'card.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/card.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='card.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
