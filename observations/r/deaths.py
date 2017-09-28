# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def deaths(path):
  """Monthly Deaths from Lung Diseases in the UK

  A time series giving the monthly deaths from bronchitis, emphysema and
  asthma in the UK, 1974-1979, both sexes (`deaths`),

  P. J. Diggle (1990) *Time Series: A Biostatistical Introduction.*
  Oxford, table A.3

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `deaths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 72 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'deaths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/deaths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='deaths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
