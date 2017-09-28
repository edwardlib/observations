# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def air_accs(path):
  """Aircraft Crash data

  Aircraft Crash Data

  A data frame with 5666 observations on the following 7 variables.

  `Date`
      Date of Accident

  `location`
      Location of accident

  `operator`
      Aircraft operator

  `planeType`
      Aircraft type

  `Dead`
      Number of deaths

  `Aboard`
      Number aboard

  `Ground`
      Deaths on ground

  http://www.planecrashinfo.com/database.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `air_accs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5666 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'air_accs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/gamclass/airAccs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='air_accs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
