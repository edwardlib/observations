# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def robey(path):
  """Fertility and Contraception

  The `Robey` data frame has 50 rows and 3 columns. The observations are
  developing nations around 1990.

  This data frame contains the following columns:

  region
      A factor with levels: `Africa`; `Asia`, Asia and Pacific;
      `Latin.Amer`, Latin America and Caribbean; `Near.East`, Near
      East and North Africa.

  tfr
      Total fertility rate (children per woman).

  contraceptors
      Percent of contraceptors among married women of childbearing age.

  Robey, B., Shea, M. A., Rutstein, O. and Morris, L. (1992) The
  reproductive revolution: New survey findings. *Population Reports*.
  Technical Report M-11.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `robey.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'robey.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Robey.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='robey.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
