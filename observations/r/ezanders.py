# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ezanders(path):
  """ezanders

  Data loads lazily. Type data(ezanders) into the console.

  A data.frame with 108 rows and 25 variables:

  -  month. name of month

  -  uclms. unemployment claims

  -  ez. =1 if enterprise zone

  -  year. 1980 through 1988

  -  y81. =1 if year == 1981

  -  y82.

  -  y83.

  -  y84.

  -  y85.

  -  y86.

  -  y87.

  -  y88.

  -  luclms. log(uclms)

  -  jan. =1 if month == JAN

  -  feb.

  -  mar.

  -  apr.

  -  may.

  -  jun.

  -  jul.

  -  aug.

  -  sep.

  -  oct.

  -  nov.

  -  dec.

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ezanders.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 108 rows and 25 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ezanders.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/ezanders.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ezanders.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
