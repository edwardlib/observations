# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def murder(path):
  """murder

  Data loads lazily. Type data(murder) into the console.

  A data.frame with 153 rows and 13 variables:

  -  id. state identifier

  -  state. postal code

  -  year. 87, 90, or 93

  -  mrdrte. murders per 100,000 people

  -  exec. total executions, past 3 years

  -  unem. annual unem. rate

  -  d90. =1 if year == 90

  -  d93. =1 if year == 93

  -  cmrdrte. mrdrte - mrdrte[\_n-1]

  -  cexec. exec - exec[\_n-1]

  -  cunem. unem - unem[\_n-1]

  -  cexec\_1. cexec[\_n-1]

  -  cunem\_1. cunem[\_n-1]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `murder.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 153 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'murder.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/murder.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='murder.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
