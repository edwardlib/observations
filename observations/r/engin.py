# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def engin(path):
  """engin

  Data loads lazily. Type data(engin) into the console.

  A data.frame with 403 rows and 17 variables:

  -  male. =1 if male

  -  educ. highest grade completed

  -  wage. monthly salary, Thai baht

  -  swage. starting wage

  -  exper. years on current job

  -  pexper. previous experience

  -  lwage. log(wage)

  -  expersq. exper^2

  -  highgrad. =1 if high school graduate

  -  college. =1 if college graduate

  -  grad. =1 if some graduate school

  -  polytech. =1 if a polytech

  -  highdrop. =1 if no high school degree

  -  lswage. log(swage)

  -  pexpersq. pexper^2

  -  mleeduc. male\*educ

  -  mleeduc0. male\*(educ - 14)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `engin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 403 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'engin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/engin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='engin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
