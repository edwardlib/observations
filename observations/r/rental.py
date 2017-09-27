# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rental(path):
  """rental

  Data loads lazily. Type data(rental) into the console.

  A data.frame with 128 rows and 23 variables:

  -  city. city label, 1 to 64

  -  year. 80 or 90

  -  pop. city population

  -  enroll. # college students enrolled

  -  rent. average rent

  -  rnthsg. renter occupied units

  -  tothsg. occupied housing units

  -  avginc. per capita income

  -  lenroll. log(enroll)

  -  lpop. log(pop)

  -  lrent. log(rent)

  -  ltothsg. log(tothsg)

  -  lrnthsg. log(rnthsg)

  -  lavginc. log(avginc)

  -  clenroll. change in lrent from 80 to 90

  -  clpop. change in lpop

  -  clrent. change in lrent

  -  cltothsg. change in ltothsg

  -  clrnthsg. change in lrnthsg

  -  clavginc. change in lavginc

  -  pctstu. percent of population students

  -  cpctstu. change in pctstu

  -  y90. =1 if year == 90

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rental.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 128 rows and 23 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rental.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/rental.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rental.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
