# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def caravan(path):
  """The Insurance Company (TIC) Benchmark

  The data contains 5822 real customer records. Each record consists of 86
  variables, containing sociodemographic data (variables 1-43) and product
  ownership (variables 44-86). The sociodemographic data is derived from
  zip codes. All customers living in areas with the same zip code have the
  same sociodemographic attributes. Variable 86 (`Purchase`) indicates
  whether the customer purchased a caravan insurance policy. Further
  information on the individual variables can be obtained at
  http://www.liacs.nl/~putten/library/cc2000/data.html

  A data frame with 5822 observations on 86 variables.

  The data was originally supplied by Sentient Machine Research and was
  used in the CoIL Challenge 2000.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `caravan.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5822 rows and 86 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'caravan.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/ISLR/Caravan.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='caravan.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
