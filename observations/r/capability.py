# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def capability(path):
  """Simulated Manufacturing Process Data

  The `capability` data frame has 75 rows and 1 columns.

  The data are simulated successive observations from a process in
  equilibrium. The process is assumed to have specification limits (5.49,
  5.79).

  This data frame contains the following column:

  `y`
      The simulated measurements.

  The data were obtained from

  Bissell, A.F. (1990) How reliable is your capability index? *Applied
  Statistics*, **39**, 331–340.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `capability.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 75 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'capability.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/capability.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='capability.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
