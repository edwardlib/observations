# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hprice2(path):
  """hprice2

  Data loads lazily. Type data(hprice2) into the console.

  A data.frame with 506 rows and 12 variables:

  -  price. median housing price, $

  -  crime. crimes committed per capita

  -  nox. nit ox concen; parts per 100m

  -  rooms. avg number of rooms

  -  dist. wght dist to 5 employ centers

  -  radial. access. index to rad. hghwys

  -  proptax. property tax per $1000

  -  stratio. average student-teacher ratio

  -  lowstat. perc of people 'lower status'

  -  lprice. log(price)

  -  lnox. log(nox)

  -  lproptax. log(proptax)

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hprice2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 506 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hprice2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/hprice2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hprice2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
