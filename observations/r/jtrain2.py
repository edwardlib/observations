# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def jtrain2(path):
  """jtrain2

  Data loads lazily. Type data(jtrain2) into the console.

  A data.frame with 445 rows and 19 variables:

  -  train. =1 if assigned to job training

  -  age. age in 1977

  -  educ. years of education

  -  black. =1 if black

  -  hisp. =1 if Hispanic

  -  married. =1 if married

  -  nodegree. =1 if no high school degree

  -  mosinex. # mnths prior to 1/78 in expmnt

  -  re74. real earns., 1974, $1000s

  -  re75. real earns., 1975, $1000s

  -  re78. real earns., 1978, $1000s

  -  unem74. =1 if unem. all of 1974

  -  unem75. =1 if unem. all of 1975

  -  unem78. =1 if unem. all of 1978

  -  lre74. log(re74); zero if re74 == 0

  -  lre75. log(re75); zero if re75 == 0

  -  lre78. log(re78); zero if re78 == 0

  -  agesq. age^2

  -  mostrn. months in training

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `jtrain2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 445 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'jtrain2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/jtrain2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='jtrain2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
