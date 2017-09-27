# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fasttrakg(path):
  """fasttrakg

  Data are from the Canadian National Cardiovascular Disease registry
  called, FASTRAK. years covered at 1996-1998. They have been grouped by
  covariate patterns from individual observations.

  A data frame with 15 observations on the following 9 variables.

  `die`
      number died from MI

  `cases`
      number of cases with same covariate pattern

  `anterior`
      1=anterior site MI; 0=inferior site MI

  `hcabg`
      1=history of CABG; 0=no history of CABG

  `killip`
      Killip level of cardiac event severity (1-4)age75

  1= Age>75; 0=Age<=75

  `kk1`
      (1/0) angina; not MI

  `kk2`
      (1/0) moderate severity cardiac event

  `kk3`
      (1/0) Severe cardiac event

  `kk4`
      (1/0) Severe cardiac event; death

  1996-1998 FASTRAK data, Hoffman-LaRoche Canada, National Health
  Economics & Research Co.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fasttrakg.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fasttrakg.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/fasttrakg.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fasttrakg.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
