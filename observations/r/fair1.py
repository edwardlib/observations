# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fair1(path):
  """fair

  Data loads lazily. Type data(fair) into the console.

  A data.frame with 21 rows and 28 variables:

  -  year. 1916 to 1992, by 4

  -  V. prop. dem. vote

  -  I. =1 if demwh, -1 if repwh

  -  DPER. incumbent running

  -  DUR. duration

  -  g3. avg ann grwth rte, prev 3 qrts

  -  p15. avg ann inf rate, prev 15 qtrs

  -  n. quarters of good news

  -  g2. avg ann grwth rte, prev 2 qrts

  -  gYR. ann grwth rte, prev year

  -  p8. avg ann inf rate, prev 8 qtrs

  -  p2YR. inf rte over 2 yr period

  -  Ig2. I\*g2

  -  Ip8. I\*p8

  -  demwins. =1 if V > .5

  -  In. I\*n

  -  d. =1 in 1920, 1944,1948

  -  Id. I\*d

  -  Ig3. I\*g3

  -  Ip151md. I\*p15\*(1-d)

  -  In1md. I\*n\*(1-d)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fair1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 28 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fair1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/fair.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fair1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
