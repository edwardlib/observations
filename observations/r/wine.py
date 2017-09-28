# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wine(path):
  """wine

  Data loads lazily. Type data(wine) into the console.

  A data.frame with 21 rows and 5 variables:

  -  country.

  -  alcohol. liters alcohol from wine, per capita

  -  deaths. deaths per 100,000

  -  heart. heart disease dths per 100,000

  -  liver. liver disease dths per 100,000

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_
  isbn_issn=9781111531041

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wine.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 21 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wine.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/wooldridge/wine.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wine.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
