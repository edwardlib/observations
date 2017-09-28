# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def houseprices(path):
  """Aranda House Prices

  The `houseprices` data frame consists of the floor area, price, and
  the number of bedrooms for a sample of houses sold in Aranda in 1999.
  Aranda is a suburb of Canberra, Australia.

  This data frame contains the following columns:

  area
      a numeric vector giving the floor area

  bedrooms
      a numeric vector giving the number of bedrooms

  sale.price
      a numeric vector giving the sale price in thousands of Australian
      dollars

  J.H. Maindonald

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `houseprices.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'houseprices.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/houseprices.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='houseprices.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
