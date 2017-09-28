# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_stamps(path):
  """USstamps

  Price of US stamp for first class mail 1885-2012

  A dataset with 25 observations on the following 2 variables.

  `Year`

  Years when stamp price changed

  `Price`

  Cost of a US first class stamp (in cents)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_stamps.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_stamps.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/USstamps.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_stamps.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
