# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hseinv(path):
  """hseinv

  Data loads lazily. Type data(hseinv) into the console.

  A data.frame with 42 rows and 14 variables:

  -  year. 1947-1988

  -  inv. real housing inv, millions $

  -  pop. population, 1000s

  -  price. housing price index; 1982 = 1

  -  linv. log(inv)

  -  lpop. log(pop)

  -  lprice. log(price)

  -  t. time trend: t=1,...,42

  -  invpc. per capita inv: inv/pop

  -  linvpc. log(invpc)

  -  lprice\_1. lprice[\_n-1]

  -  linvpc\_1. linvpc[\_n-1]

  -  gprice. lprice - lprice\_1

  -  ginvpc. linvpc - linvpc\_1

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hseinv.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 42 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hseinv.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/hseinv.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hseinv.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
