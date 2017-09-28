# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def water(path):
  """Mortality and Water Hardness

  The mortality and drinking water hardness for 61 cities in England and
  Wales.

  A data frame with 61 observations on the following 4 variables.

  location
      a factor with levels `North` and `South` indicating whether the
      town is as north as Derby.

  town
      the name of the town.

  mortality
      averaged annual mortality per 100.000 male inhabitants.

  hardness
      calcium concentration (in parts per million).

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `water.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 61 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'water.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/water.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='water.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
