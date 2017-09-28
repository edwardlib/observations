# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def meap93(path):
  """meap93

  Data loads lazily. Type data(meap93) into the console.

  A data.frame with 408 rows and 17 variables:

  -  lnchprg. perc of studs in sch lnch prog

  -  enroll. school enrollment

  -  staff. staff per 1000 students

  -  expend. expend. per stud, $

  -  salary. avg. teacher salary, $

  -  benefits. avg. teacher benefits, $

  -  droprate. school dropout rate, perc

  -  gradrate. school graduation rate, perc

  -  math10. perc studs passing MEAP math

  -  sci11. perc studs passing MEAP science

  -  totcomp. salary + benefits

  -  ltotcomp. log(totcomp)

  -  lexpend. log of expend

  -  lenroll. log(enroll)

  -  lstaff. log(staff)

  -  bensal. benefits/salary

  -  lsalary. log(salary)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `meap93.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 408 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'meap93.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/meap93.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='meap93.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
