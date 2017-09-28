# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crime1(path):
  """crime1

  Data loads lazily. Type data(crime1) into the console.

  A data.frame with 2725 rows and 16 variables:

  -  narr86. # times arrested, 1986

  -  nfarr86. # felony arrests, 1986

  -  nparr86. # property crme arr., 1986

  -  pcnv. proportion of prior convictions

  -  avgsen. avg sentence length, mos.

  -  tottime. time in prison since 18 (mos.)

  -  ptime86. mos. in prison during 1986

  -  qemp86. # quarters employed, 1986

  -  inc86. legal income, 1986, $100s

  -  durat. recent unemp duration

  -  black. =1 if black

  -  hispan. =1 if Hispanic

  -  born60. =1 if born in 1960

  -  pcnvsq. pcnv^2

  -  pt86sq. ptime86^2

  -  inc86sq. inc86^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crime1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2725 rows and 16 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crime1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/crime1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crime1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
