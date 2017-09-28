# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def frets(path):
  """Head Dimensions in Brothers

  The `frets` data frame has 25 rows and 4 columns.

  The data consist of measurements of the length and breadth of the heads
  of pairs of adult brothers in 25 randomly sampled families. All
  measurements are expressed in millimetres.

  This data frame contains the following columns:

  `l1`
      The head length of the eldest son.

  `b1`
      The head breadth of the eldest son.

  `l2`
      The head length of the second son.

  `b2`
      The head breadth of the second son.

  The data were obtained from

  Frets, G.P. (1921) Heredity of head form in man. *Genetica*, **3**, 193.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `frets.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'frets.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/frets.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='frets.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
