# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def austpop(path):
  """Population figures for Australian States and Territories

  Population figures for Australian states and territories for 1917, 1927,
  ..., 1997.

  This data frame contains the following columns:

  year
      a numeric vector

  NSW
      New South Wales population counts

  Vic
      Victoria population counts

  Qld
      Queensland population counts

  SA
      South Australia population counts

  WA
      Western Australia population counts

  Tas
      Tasmania population counts

  NT
      Northern Territory population counts

  ACT
      Australian Capital Territory population counts

  Aust
      Population counts for the whole country

  Australian Bureau of Statistics

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `austpop.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'austpop.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/austpop.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='austpop.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
