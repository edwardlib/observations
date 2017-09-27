# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lawsch85(path):
  """lawsch85

  Data loads lazily. Type data(lawsch85) into the console.

  A data.frame with 156 rows and 21 variables:

  -  rank. law school ranking

  -  salary. median starting salary

  -  cost. law school cost

  -  LSAT. median LSAT score

  -  GPA. median college GPA

  -  libvol. no. volumes in lib., 1000s

  -  faculty. no. of faculty

  -  age. age of law sch., years

  -  clsize. size of entering class

  -  north. =1 if law sch in north

  -  south. =1 if law sch in south

  -  east. =1 if law sch in east

  -  west. =1 if law sch in west

  -  lsalary. log(salary)

  -  studfac. student-faculty ratio

  -  top10. =1 if ranked in top 10

  -  r11\_25. =1 if ranked 11-25

  -  r26\_40. =1 if ranked 26-40

  -  r41\_60. =1 if ranked 41-60

  -  llibvol. log(libvol)

  -  lcost. log(cost)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lawsch85.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 156 rows and 21 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lawsch85.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/lawsch85.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lawsch85.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
