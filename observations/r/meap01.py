from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def meap01(path):
  """meap01

  Data loads lazily. Type data(meap01) into the console.

  A data.frame with 1823 rows and 11 variables:

  -  dcode. district code

  -  bcode. building code

  -  math4. percent students satisfactory, 4th grade math

  -  read4. percent students satisfactory, 4th grade reading

  -  lunch. percent students eligible for free or reduced lunch

  -  enroll. school enrollment

  -  expend. total spending, $

  -  exppp. expenditures per pupil: expend/enroll

  -  lenroll. log(enroll)

  -  lexpend. log(expend)

  -  lexppp. log(exppp)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `meap01.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1823 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'meap01.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/wooldridge/meap01.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='meap01.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
