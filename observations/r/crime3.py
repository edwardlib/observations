# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crime3(path):
  """crime3

  Data loads lazily. Type data(crime3) into the console.

  A data.frame with 106 rows and 12 variables:

  -  district. district number

  -  year. 72 or 78

  -  crime. crimes per 1000 people

  -  clrprc1. clear-up perc, prior year

  -  clrprc2. clear-up perc, two-years prior

  -  d78. =1 if year = 78

  -  avgclr. (clrprc1 + clrprc2)/2

  -  lcrime. log(crime)

  -  clcrime. change in lcrime

  -  cavgclr. change in avgclr

  -  cclrprc1. change in clrprc1

  -  cclrprc2. change in clrprc2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crime3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 106 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crime3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/crime3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crime3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
