# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def shuttle(path):
  """Space Shuttle Autolander Problem

  The `shuttle` data frame has 256 rows and 7 columns. The first six
  columns are categorical variables giving example conditions; the seventh
  is the decision. The first 253 rows are the training set, the last 3 the
  test conditions.

  This data frame contains the following factor columns:

  `stability`
      stable positioning or not (`stab` / `xstab`).

  `error`
      size of error (`MM` / `SS` / `LX` / `XL`).

  `sign`
      sign of error, positive or negative (`pp` / `nn`).

  `wind`
      wind sign (`head` / `tail`).

  `magn`
      wind strength (`Light` / `Medium` / `Strong` /
      `Out of Range`).

  `vis`
      visibility (`yes` / `no`).

  `use`
      use the autolander or not. (`auto` / `noauto`.)

  D. Michie (1989) Problems of computer-aided concept formation. In
  *Applications of Expert Systems 2*, ed. J. R. Quinlan, Turing Institute
  Press / Addison-Wesley, pp. 310–333.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `shuttle.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 256 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'shuttle.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/shuttle.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='shuttle.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
