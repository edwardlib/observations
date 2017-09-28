# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fertil3(path):
  """fertil3

  Data loads lazily. Type data(fertil3) into the console.

  A data.frame with 72 rows and 24 variables:

  -  gfr. births per 1000 women 15-44

  -  pe. real value pers. exemption, $

  -  year. 1913 to 1984

  -  t. time trend, t=1,...,72

  -  tsq. t^2

  -  pe\_1. pe[\_n-1]

  -  pe\_2. pe[\_n-2]

  -  pe\_3. pe[\_n-3]

  -  pe\_4. pe[\_n-4]

  -  pill. =1 if year >= 1963

  -  ww2. =1, 1941 to 1945

  -  tcu. t^3

  -  cgfr. change in gfr: gfr - gfr\_1

  -  cpe. pe - pe\_1

  -  cpe\_1. cpe[\_n-1]

  -  cpe\_2. cpe[\_n-2]

  -  cpe\_3. cpe[\_n-3]

  -  cpe\_4. cpe[\_n-4]

  -  gfr\_1. gfr[\_n-1]

  -  cgfr\_1. cgfr[\_n-1]

  -  cgfr\_2. cgfr[\_n-2]

  -  cgfr\_3. cgfr[\_n-3]

  -  cgfr\_4. cgfr[\_n-4]

  -  gfr\_2. gfr[\_n-2]

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fertil3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 24 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fertil3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/fertil3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fertil3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
