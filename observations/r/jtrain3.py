# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def jtrain3(path):
  """jtrain3

  Data loads lazily. Type data(jtrain3) into the console.

  A data.frame with 2675 rows and 20 variables:

  -  train. =1 if in job training

  -  age. in years, 1977

  -  educ. years of schooling

  -  black. =1 if black

  -  hisp. =1 if Hispanic

  -  married. =1 if married

  -  re74. '74 earnings, $1000s '82

  -  re75. '75 earnings, $1000s '82

  -  unem75. =1 if unem. all of '75

  -  unem74. =1 if unem. all of '74

  -  re78. '78 earnings, $1000s '82

  -  agesq. age^2

  -  trre74. train\*re74

  -  trre75. train\*re75

  -  trun74. train\*unem74

  -  trun75. train\*unem75

  -  avgre. (re74 + re75)/2

  -  travgre. train\*avgre

  -  unem78. =1 if unem. all of '78

  -  em78. 1 - unem78

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `jtrain3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2675 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'jtrain3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/jtrain3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='jtrain3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
