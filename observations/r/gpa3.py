# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gpa3(path):
  """gpa3

  Data loads lazily. Type data(gpa3) into the console.

  A data.frame with 732 rows and 23 variables:

  -  term. fall = 1, spring = 2

  -  sat. SAT score

  -  tothrs. total hours prior to term

  -  cumgpa. cumulative GPA

  -  season. =1 if in season

  -  frstsem. =1 if student's 1st semester

  -  crsgpa. weighted course GPA

  -  verbmath. verbal SAT to math SAT ratio

  -  trmgpa. term GPA

  -  hssize. size h.s. grad. class

  -  hsrank. rank in h.s. class

  -  id. student identifier

  -  spring. =1 if spring term

  -  female. =1 if female

  -  black. =1 if black

  -  white. =1 if white

  -  ctrmgpa. change in trmgpa

  -  ctothrs. change in total hours

  -  ccrsgpa. change in crsgpa

  -  ccrspop. change in crspop

  -  cseason. change in season

  -  hsperc. percentile in h.s.

  -  football. =1 if football player

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gpa3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 732 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gpa3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/gpa3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gpa3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
