# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def intqrt(path):
  """intqrt

  Data loads lazily. Type data(intqrt) into the console.

  A data.frame with 124 rows and 23 variables:

  -  r3. bond equiv. yield, 3 mo T-bill

  -  r6. bond equiv. yield, 6 mo T-bill

  -  r12. yield on 1 yr. bond

  -  p3. price of 3 mo. T-bill

  -  p6. price of 6 mo. T-bill

  -  hy6. 100\*(p3 - p6[\_n-1])/p6[\_n-1])

  -  hy3. r3\*(91/365)

  -  spr63. r6 - r3

  -  hy3\_1. hy3[\_n-1]

  -  hy6\_1. hy6[\_n-1]

  -  spr63\_1. spr63[\_n-1]

  -  hy6hy3\_1. hy6 - hy3\_1

  -  cr3. r3 - r3\_1

  -  r3\_1. r3[\_n-1]

  -  chy6. hy6 - hy6\_1

  -  chy3. hy3 - hy3\_1

  -  chy6\_1. chy6[\_n-1]

  -  chy3\_1. chy3[\_n-1]

  -  cr6. r6 - r6\_1

  -  cr6\_1. cr6[\_n-1]

  -  cr3\_1. cr3[\_n-1]

  -  r6\_1. r6[\_n-1]

  -  cspr63. spr63 - spr63\_1

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `intqrt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 124 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'intqrt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/intqrt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='intqrt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
