# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gpa1(path):
  """gpa1

  Data loads lazily. Type data(gpa1) into the console.

  A data.frame with 141 rows and 29 variables:

  -  age. in years

  -  soph. =1 if sophomore

  -  junior. =1 if junior

  -  senior. =1 if senior

  -  senior5. =1 if fifth year senior

  -  male. =1 if male

  -  campus. =1 if live on campus

  -  business. =1 if business major

  -  engineer. =1 if engineering major

  -  colGPA. MSU GPA

  -  hsGPA. high school GPA

  -  ACT. 'achievement' score

  -  job19. =1 if job <= 19 hours

  -  job20. =1 if job >= 20 hours

  -  drive. =1 if drive to campus

  -  bike. =1 if bicycle to campus

  -  walk. =1 if walk to campus

  -  voluntr. =1 if do volunteer work

  -  PC. =1 of pers computer at sch

  -  greek. =1 if fraternity or sorority

  -  car. =1 if own car

  -  siblings. =1 if have siblings

  -  bgfriend. =1 if boy- or girlfriend

  -  clubs. =1 if belong to MSU club

  -  skipped. avg lectures missed per week

  -  alcohol. avg # days per week drink alc.

  -  gradMI. =1 if Michigan high school

  -  fathcoll. =1 if father college grad

  -  mothcoll. =1 if mother college grad

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gpa1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 141 rows and 29 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gpa1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/gpa1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gpa1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
