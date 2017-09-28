# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def htv(path):
  """htv

  Data loads lazily. Type data(htv) into the console.

  A data.frame with 1230 rows and 23 variables:

  -  wage. hourly wage, 1991

  -  abil. abil. measure, not standardized

  -  educ. highest grade completed by 1991

  -  ne. =1 if in northeast, 1991

  -  nc. =1 if in nrthcntrl, 1991

  -  west. =1 if in west, 1991

  -  south. =1 if in south, 1991

  -  exper. potential experience

  -  motheduc. highest grade, mother

  -  fatheduc. highest grade, father

  -  brkhme14. =1 if broken home, age 14

  -  sibs. number of siblings

  -  urban. =1 if in urban area, 1991

  -  ne18. =1 if in NE, age 18

  -  nc18. =1 if in NC, age 18

  -  south18. =1 if in south, age 18

  -  west18. =1 if in west, age 18

  -  urban18. =1 if in urban area, age 18

  -  tuit17. college tuition, age 17

  -  tuit18. college tuition, age 18

  -  lwage. log(wage)

  -  expersq. exper^2

  -  ctuit. tuit18 - tuit17

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `htv.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1230 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'htv.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/htv.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='htv.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
