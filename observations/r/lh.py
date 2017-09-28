# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lh(path):
  """Luteinizing Hormone in Blood Samples

  A regular time series giving the luteinizing hormone in blood samples at
  10 mins intervals from a human female, 48 samples.

  P.J. Diggle (1990) *Time Series: A Biostatistical Introduction.* Oxford,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lh.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lh.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/lh.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lh.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
