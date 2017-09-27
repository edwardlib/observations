# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nile(path):
  """Flow of the River Nile

  Measurements of the annual flow of the river Nile at Aswan (formerly
  `Assuan`), 1871–1970, in *10^8 m^3*, “with apparent changepoint near
  1898” (Cobb(1978), Table 1, p.249).

  A time series of length 100.

  Durbin, J. and Koopman, S. J. (2001) *Time Series Analysis by State
  Space Methods.* Oxford University Press.
  http://www.ssfpack.com/DKbook.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nile.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nile.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/Nile.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nile.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
