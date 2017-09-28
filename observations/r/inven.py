# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def inven(path):
  """inven

  Data loads lazily. Type data(inven) into the console.

  A data.frame with 37 rows and 13 variables:

  -  year. 1959-1995

  -  i3. 3 mo. T-bill rate

  -  inf. CPI inflation rate

  -  inven. inventories, billions '92 $

  -  gdp. GDP, billions '92 $

  -  r3. real interest: i3 - inf

  -  cinven. inven - inven[\_n-1]

  -  cgdp. gdp - gdp[\_n-1]

  -  cr3. r3 - r3[\_n-1]

  -  ci3. i3 - i3[\_n-1]

  -  cinf. inf - inf[\_n-1]

  -  ginven. log(inven) - log(inven[\_n-1])

  -  ggdp. log(gdp) - log(gdp[\_n-1])

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `inven.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'inven.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/inven.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='inven.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
