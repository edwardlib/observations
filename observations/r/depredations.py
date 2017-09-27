# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def depredations(path):
  """Minnesota Wolf Depredation Data

  Wolf depredations of livestock on Minnesota farms, 1976-1998.

  A data frame with 434 observations on the following 5 variables.

  `longitude`
      longitude of the farm

  `latitude`
      latitude of the farm

  `number`
      number of depredations 1976-1998

  `early`
      number of depredations 1991 or before

  `late`
      number of depredations 1992 or later

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `depredations.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 434 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'depredations.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Depredations.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='depredations.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
