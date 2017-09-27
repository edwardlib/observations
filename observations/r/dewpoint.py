# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dewpoint(path):
  """Dewpoint Data

  The `dewpoint` data frame has 72 rows and 3 columns. Monthly data were
  obtained for a number of sites (in Australia) and a number of months.

  This data frame contains the following columns:

  maxtemp
      monthly minimum temperatures

  mintemp
      monthly maximum temperatures

  dewpt
      monthly average dewpoint for each combination of minimum and maximum
      temperature readings (formerly dewpoint)

  Dr Edward Linacre, visiting fellow in the Australian National University
  Department of Geography.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dewpoint.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dewpoint.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/dewpoint.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dewpoint.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
