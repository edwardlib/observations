# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ezunem(path):
  """ezunem

  Data loads lazily. Type data(ezunem) into the console.

  A data.frame with 198 rows and 37 variables:

  -  year. 1980 to 1988

  -  uclms. unemployment claims

  -  ez. =1 if have enterprise zone

  -  d81. =1 if year == 1981

  -  d82. =1 if year == 1982

  -  d83. =1 if year == 1983

  -  d84. =1 if year == 1984

  -  d85. =1 if year == 1985

  -  d86. =1 if year == 1986

  -  d87. =1 if year == 1987

  -  d88. =1 if year == 1988

  -  c1. =1 if city == 1

  -  c2. =1 if city == 2

  -  c3. =1 if city == 3

  -  c4.

  -  c5.

  -  c6.

  -  c7.

  -  c8.

  -  c9.

  -  c10.

  -  c11.

  -  c12.

  -  c13.

  -  c14.

  -  c15.

  -  c16.

  -  c17.

  -  c18.

  -  c19.

  -  c20.

  -  c21.

  -  c22. =1 if city == 22

  -  luclms. log(uclms)

  -  guclms. luclms - luclms[\_n-1]

  -  cez. ez - ez[\_n-1]

  -  city. city identifier, 1 through 22

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ezunem.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 198 rows and 37 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ezunem.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/ezunem.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ezunem.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
