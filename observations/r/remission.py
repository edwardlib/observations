# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def remission(path):
  """Cancer Remission and Cell Activity

  The `remission` data frame has 27 rows and 3 columns.

  This data frame contains the following columns:

  `LI`
      A measure of cell activity.

  `m`
      The number of patients in each group (all values are actually 1
      here).

  `r`
      The number of patients (out of `m`) who went into remission.

  The data were obtained from

  Freeman, D.H. (1987) *Applied Categorical Data Analysis*. Marcel Dekker.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `remission.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'remission.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/remission.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='remission.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
