# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def strike(path):
  """Strike Duration Data

  a cross-section from 1968 to 1976

  *number of observations* : 62

  *country* : United States

  A dataframe containing :

  duration
      strike duration in days

  prod
      unanticipated output

  Kennan, J. (1985) “The duration of contract strikes in U.S.
  manufacturing”, *Journal of Econometrics*, **28**, 5-28.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `strike.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'strike.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Strike.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='strike.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
