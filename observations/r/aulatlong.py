# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aulatlong(path):
  """Latitudes and longitudes for ten Australian cities

  Latitudes and longitudes for Adelaide, Alice, Brisbane, Broome, Cairns,
  Canberra, Darwin, Melbourne, Perth and Sydney; i.e., for the cities to
  which the road distances in `audists` relate.

  A data frame with 10 observations on the following 2 variables.

  `latitude`
      Latitude, as a decimal number

  `longitude`
      Latitude, as a decimal number

  Map of Australia showing latitude and longitude information.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aulatlong.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aulatlong.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/aulatlong.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aulatlong.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
