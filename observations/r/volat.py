# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def volat(path):
  """volat

  Data loads lazily. Type data(volat) into the console.

  A data.frame with 558 rows and 17 variables:

  -  date. 1947.01 to 1993.06

  -  sp500. S&P 500 index

  -  divyld. div. yield annualized rate

  -  i3. 3 mo. T-bill annualized rate

  -  ip. index of industrial production

  -  pcsp. pct chg, sp500, ann rate

  -  rsp500. return on sp500: pcsp + divyld

  -  pcip. pct chg, IP, ann rate

  -  ci3. i3 - i3[\_n-1]

  -  ci3\_1. ci3[\_n-1]

  -  ci3\_2. ci3[\_n-2]

  -  pcip\_1. pcip[\_n-1]

  -  pcip\_2. pcip[\_n-2]

  -  pcip\_3. pcip[\_n-3]

  -  pcsp\_1. pcip[\_n-1]

  -  pcsp\_2. pcip[\_n-2]

  -  pcsp\_3. pcip[\_n-3]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `volat.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 558 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'volat.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/volat.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='volat.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
