# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vote2(path):
  """vote2

  Data loads lazily. Type data(vote2) into the console.

  A data.frame with 186 rows and 26 variables:

  -  state. state postal code

  -  district. U.S. Congressional district

  -  democ. =1 if incumbent democrat

  -  vote90. inc. share two-party vote, 1990

  -  vote88. inc. share two-party vote, 1988

  -  inexp90. inc. camp. expends., 1990

  -  chexp90. chl. camp. expends., 1990

  -  inexp88. inc. camp. expends., 1988

  -  chexp88. chl. camp. expends., 1988

  -  prtystr. percent vote pres., same party, 1988

  -  rptchall. =1 if a repeat challenger

  -  tenure. years in H.R.

  -  lawyer. =1 if law degree

  -  linexp90. log(inexp90)

  -  lchexp90. log(chexp90)

  -  linexp88. log(inexp88)

  -  lchexp88. log(chexp88)

  -  incshr90. 100\*(inexp90/(inexp90+chexp90))

  -  incshr88. 100\*(inexp88/(inexp88+chexp88))

  -  cvote. vote90 - vote88

  -  clinexp. linexp90 - linexp88

  -  clchexp. lchexp90 - lchexp88

  -  cincshr. incshr90 - incshr88

  -  win88. =1 by definition

  -  win90. =1 if inc. wins, 1990

  -  cwin. win90 - win88

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vote2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 186 rows and 26 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vote2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/vote2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vote2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
