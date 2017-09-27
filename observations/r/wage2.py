# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wage2(path):
  """wage2

  Data loads lazily. Type data(wage2) into the console.

  A data.frame with 935 rows and 17 variables:

  -  wage. monthly earnings

  -  hours. average weekly hours

  -  IQ. IQ score

  -  KWW. knowledge of world work score

  -  educ. years of education

  -  exper. years of work experience

  -  tenure. years with current employer

  -  age. age in years

  -  married. =1 if married

  -  black. =1 if black

  -  south. =1 if live in south

  -  urban. =1 if live in SMSA

  -  sibs. number of siblings

  -  brthord. birth order

  -  meduc. mother's education

  -  feduc. father's education

  -  lwage. natural log of wage

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wage2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 935 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wage2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/wage2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wage2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
