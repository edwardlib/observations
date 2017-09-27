# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def births78(path):
  """US Births in 1978

  A day by day record of the number of births in the United States in
  1978.

  A data frame with 365 observations on the following variables.

  -  `date` date in 1978

  -  `births` number of US births

  -  `dayofyear` sequential number of days from 1 to 365

  -  `wday` day of week as an ordered factor

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `births78.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 365 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'births78.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Births78.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='births78.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
