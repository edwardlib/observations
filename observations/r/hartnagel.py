# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hartnagel(path):
  """Canadian Crime-Rates Time Series

  The `Hartnagel` data frame has 38 rows and 7 columns. The data are an
  annual time-series from 1931 to 1968. There are some missing data.

  This data frame contains the following columns:

  year
      1931–1968.

  tfr
      Total fertility rate per 1000 women.

  partic
      Women's labor-force participation rate per 1000.

  degrees
      Women's post-secondary degree rate per 10,000.

  fconvict
      Female indictable-offense conviction rate per 100,000.

  ftheft
      Female theft conviction rate per 100,000.

  mconvict
      Male indictable-offense conviction rate per 100,000.

  mtheft
      Male theft conviction rate per 100,000.

  Personal communication from T. Hartnagel, Department of Sociology,
  University of Alberta.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hartnagel.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hartnagel.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Hartnagel.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hartnagel.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
