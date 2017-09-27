# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gpa2(path):
  """gpa2

  Data loads lazily. Type data(gpa2) into the console.

  A data.frame with 4137 rows and 12 variables:

  -  sat. combined SAT score

  -  tothrs. total hours through fall semest

  -  colgpa. GPA after fall semester

  -  athlete. =1 if athlete

  -  verbmath. verbal/math SAT score

  -  hsize. size grad. class, 100s

  -  hsrank. rank in grad. class

  -  hsperc. high school percentile, from top

  -  female. =1 if female

  -  white. =1 if white

  -  black. =1 if black

  -  hsizesq. hsize^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gpa2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4137 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gpa2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/gpa2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gpa2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
