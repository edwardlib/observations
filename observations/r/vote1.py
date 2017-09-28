# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vote1(path):
  """vote1

  Data loads lazily. Type data(vote1) into the console.

  A data.frame with 173 rows and 10 variables:

  -  state. state postal code

  -  district. congressional district

  -  democA. =1 if A is democrat

  -  voteA. percent vote for A

  -  expendA. camp. expends. by A, $1000s

  -  expendB. camp. expends. by B, $1000s

  -  prtystrA. percent vote for president

  -  lexpendA. log(expendA)

  -  lexpendB. log(expendB)

  -  shareA. 100\*(expendA/(expendA+expendB))

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vote1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 173 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vote1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/vote1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vote1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
