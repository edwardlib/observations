# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def elem94_95(path):
  """elem94\_95

  Data loads lazily. Type data(elem94\_95) into the console.

  A data.frame with 1848 rows and 14 variables:

  -  distid. district identifier

  -  schid. school identifier

  -  lunch. percent eligible, free lunch

  -  enrol. enrollment

  -  staff. staff per 1000 students

  -  exppp. expenditures per pupil

  -  avgsal. average teacher salary, $

  -  avgben. average teacher non-salary benefits, $

  -  math4. percent passing 4th grade math test

  -  story4. percent passing 4th grade reading test

  -  bs. avgben/avgsal

  -  lavgsal. log(avgsal)

  -  lenrol. log(enrol)

  -  lstaff. log(staff)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `elem94_95.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1848 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'elem94_95.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/elem94_95.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='elem94_95.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
