# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pntsprd(path):
  """pntsprd

  Data loads lazily. Type data(pntsprd) into the console.

  A data.frame with 553 rows and 12 variables:

  -  favscr. favored team's score

  -  undscr. underdog's score

  -  spread. las vegas spread

  -  favhome. =1 if favored team at home

  -  neutral. =1 if neutral site

  -  fav25. =1 if favored team in top 25

  -  und25. =1 if underdog in top 25

  -  fregion. favorite's region of country

  -  uregion. underdog's region of country

  -  scrdiff. favscr - undscr

  -  sprdcvr. =1 if spread covered

  -  favwin. =1 if favored team wins

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pntsprd.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 553 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pntsprd.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/pntsprd.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pntsprd.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
