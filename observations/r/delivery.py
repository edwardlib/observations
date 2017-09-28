# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def delivery(path):
  """Delivery Time Data

  Delivery Time Data, from Montgomery and Peck (1982). The aim is to
  explain the time required to service a vending machine (Y) by means of
  the number of products stocked (X1) and the distance walked by the route
  driver (X2).

  A data frame with 25 observations on the following 3 variables.

  `n.prod`
      Number of Products

  `distance`
      Distance

  `delTime`
      Delivery time

  Montgomery and Peck (1982, p.116)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `delivery.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'delivery.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/delivery.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='delivery.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
