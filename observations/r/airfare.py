# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def airfare(path):
  """airfare

  Data loads lazily. Type data(airfare) into the console.

  A data.frame with 4596 rows and 14 variables:

  -  year. 1997, 1998, 1999, 2000

  -  id. route identifier

  -  dist. distance, in miles

  -  passen. avg. passengers per day

  -  fare. avg. one-way fare, $

  -  bmktshr. fraction market, biggest carrier

  -  ldist. log(distance)

  -  y98. =1 if year == 1998

  -  y99. =1 if year == 1999

  -  y00. =1 if year == 2000

  -  lfare. log(fare)

  -  ldistsq. ldist^2

  -  concen. = bmktshr

  -  lpassen. log(passen)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `airfare.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4596 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'airfare.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/airfare.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='airfare.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
