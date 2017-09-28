# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def smoke(path):
  """smoke

  Data loads lazily. Type data(smoke) into the console.

  A data.frame with 807 rows and 10 variables:

  -  educ. years of schooling

  -  cigpric. state cig. price, cents/pack

  -  white. =1 if white

  -  age. in years

  -  income. annual income, $

  -  cigs. cigs. smoked per day

  -  restaurn. =1 if rest. smk. restrictions

  -  lincome. log(income)

  -  agesq. age^2

  -  lcigpric. log(cigprice)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `smoke.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 807 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'smoke.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/smoke.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='smoke.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
