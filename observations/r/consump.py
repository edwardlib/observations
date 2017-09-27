# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def consump(path):
  """consump

  Data loads lazily. Type data(consump) into the console.

  A data.frame with 37 rows and 24 variables:

  -  year. 1959-1995

  -  i3. 3 mo. T-bill rate

  -  inf. inflation rate; CPI

  -  rdisp. disp. inc., 1992 $, bils.

  -  rnondc. nondur. cons., 1992 $, bils.

  -  rserv. services, 1992 $, bils.

  -  pop. population, 1000s

  -  y. per capita real disp. inc.

  -  rcons. rnondc + rserv

  -  c. per capita real cons.

  -  r3. i3 - inf; real ex post int.

  -  lc. log(c)

  -  ly. log(y)

  -  gc. lc - lc[\_n-1]

  -  gy. ly - ly[\_n-1]

  -  gc\_1. gc[\_n-1]

  -  gy\_1. gy[\_n-1]

  -  r3\_1. r3[\_n-1]

  -  lc\_ly. lc - ly

  -  lc\_ly\_1. lc\_ly[\_n-1]

  -  gc\_2. gc[\_n-2]

  -  gy\_2. gy[\_n-2]

  -  r3\_2. r3[\_n-2]

  -  lc\_ly\_2. lc\_ly[\_n-2]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `consump.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 37 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'consump.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/consump.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='consump.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
