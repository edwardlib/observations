# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def beauty(path):
  """beauty

  Data loads lazily. Type data(beauty) into the console.

  A data.frame with 1260 rows and 17 variables:

  -  wage. hourly wage

  -  lwage. log(wage)

  -  belavg. =1 if looks <= 2

  -  abvavg. =1 if looks >=4

  -  exper. years of workforce experience

  -  looks. from 1 to 5

  -  union. =1 if union member

  -  goodhlth. =1 if good health

  -  black. =1 if black

  -  female. =1 if female

  -  married. =1 if married

  -  south. =1 if live in south

  -  bigcity. =1 if live in big city

  -  smllcity. =1 if live in small city

  -  service. =1 if service industry

  -  expersq. exper^2

  -  educ. years of schooling

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `beauty.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1260 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'beauty.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/beauty.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='beauty.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
