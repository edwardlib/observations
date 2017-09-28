# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hprice3(path):
  """hprice3

  Data loads lazily. Type data(hprice3) into the console.

  A data.frame with 321 rows and 19 variables:

  -  year. 1978, 1981

  -  age. age of house

  -  agesq. age^2

  -  nbh. neighborhood, 1-6

  -  cbd. dist. to cent. bus. dstrct, ft.

  -  inst. dist. to interstate, ft.

  -  linst. log(inst)

  -  price. selling price

  -  rooms. # rooms in house

  -  area. square footage of house

  -  land. square footage lot

  -  baths. # bathrooms

  -  dist. dist. from house to incin., ft.

  -  ldist. log(dist)

  -  lprice. log(price)

  -  y81. =1 if year = 1981

  -  larea. log(area)

  -  lland. log(land)

  -  linstsq. linst^2

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hprice3.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 321 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hprice3.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/hprice3.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hprice3.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
