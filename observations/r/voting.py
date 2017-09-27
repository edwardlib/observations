# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def voting(path):
  """House of Representatives Voting Data

  Voting results for 15 congressmen from New Jersey.

  A 15 times 15 matrix.

  H. C. Romesburg (1984), *Cluster Analysis for Researchers*. Lifetime
  Learning Publications, Belmont, Canada.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `voting.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'voting.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/voting.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='voting.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
