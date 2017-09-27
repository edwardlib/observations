# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nbasal(path):
  """nbasal

  Data loads lazily. Type data(nbasal) into the console.

  A data.frame with 269 rows and 22 variables:

  -  marr. =1 if married

  -  wage. annual salary, thousands $

  -  exper. years as professional player

  -  age. age in years

  -  coll. years played in college

  -  games. average games per year

  -  minutes. average minutes per year

  -  guard. =1 if guard

  -  forward. =1 if forward

  -  center. =1 if center

  -  points. points per game

  -  rebounds. rebounds per game

  -  assists. assists per game

  -  draft. draft number

  -  allstar. =1 if ever all star

  -  avgmin. minutes per game

  -  lwage. log(wage)

  -  black. =1 if black

  -  children. =1 if has children

  -  expersq. exper^2

  -  agesq. age^2

  -  marrblck. marr\*black

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nbasal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 269 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nbasal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/nbasal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nbasal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
