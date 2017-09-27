# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def benefits1(path):
  """benefits

  Data loads lazily. Type data(benefits) into the console.

  A data.frame with 1848 rows and 18 variables:

  -  distid. district identifier

  -  schid. school identifier

  -  lunch. percent eligible, free lunch

  -  enroll. school enrollment

  -  staff. staff per 1000 students

  -  exppp. expenditures per pupil

  -  avgsal. average teacher salary, $

  -  avgben. average teacher non-salary benefits, $

  -  math4. percent passing 4th grade math test

  -  story4. percent passing 4th grade reading test

  -  bs. avgben/avgsal

  -  lavgsal. log(avgsal)

  -  lenroll. log(enroll)

  -  lstaff. log(staff)

  -  bsbar. within-district avg of bs

  -  lunchbar. within-district avg of lunch

  -  lenrollbar. within-district avg of lenroll

  -  lstaffbar. within-district avg of lstaff

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `benefits1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1848 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'benefits1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/benefits.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='benefits1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
