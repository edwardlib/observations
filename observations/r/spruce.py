# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def spruce(path):
  """Log-size of 79 Sitka spruce trees

  The `spruce` data frame has 1027 rows and 6 columns. The data consists
  of measurements on 79 sitka spruce trees over two growing seasons. The
  trees were grown in four controlled environment chambers, of which the
  first two, containing 27 trees each, were treated with introduced ozone
  at 70 ppb whilst the remaining two, containing 12 and 13 trees, were
  controls.

  This data frame contains the following columns:

  chamber
      a numeric vector of chamber numbers

  ozone
      a factor with levels `enriched` and `normal`

  id
      a numeric vector of tree id

  time
      a numeric vector of the time when the measurements were taken,
      measured in days since Jan. 1, 1988

  wave
      a numeric vector of the measurement number

  logsize
      a numeric vector of the log-size

  Diggle, P.J., Liang, K.Y., and Zeger, S.L. (1994) Analysis of
  Longitudinal Data, Clarendon Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `spruce.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1027 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'spruce.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/geepack/spruce.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='spruce.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
