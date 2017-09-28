# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wageprc(path):
  """wageprc

  Data loads lazily. Type data(wageprc) into the console.

  A data.frame with 286 rows and 20 variables:

  -  price. consumer price index

  -  wage. nominal hourly wage

  -  t. time trend = 1, 2 , 3, ...

  -  lprice. log(price)

  -  lwage. log(wage)

  -  gprice. lprice - lprice[\_n-1]

  -  gwage. lwage - lwage[\_n-1]

  -  gwage\_1. gwage[\_n-1]

  -  gwage\_2. gwage[\_n-2]

  -  gwage\_3.

  -  gwage\_4.

  -  gwage\_5.

  -  gwage\_6.

  -  gwage\_7.

  -  gwage\_8.

  -  gwage\_9.

  -  gwage\_10.

  -  gwage\_11.

  -  gwage\_12.

  -  gprice\_1. gprice[\_n-1]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wageprc.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 286 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wageprc.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/wageprc.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wageprc.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
