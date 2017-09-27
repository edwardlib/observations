# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def snmesp(path):
  """Employment and Wages in Spain

  A panel of 738 observations from 1983 to 1990

  *total number of observations*: 5904

  *observation*: firms

  *country*: Spain

  A data frame containing:

  firm
      firm index

  year
      year

  n
      log of employment

  w
      log of wages

  y
      log of real output

  i
      log of intermediate inputs

  k
      log of real capital stock

  f
      real cash flow

  Journal of Business Economics and Statistics data archive:

  http://amstat.tandfonline.com/loi/ubes20/.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `snmesp.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5904 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'snmesp.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/Snmesp.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='snmesp.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
