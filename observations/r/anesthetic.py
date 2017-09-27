# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def anesthetic(path):
  """Anesthetic Effectiveness

  Thirty patients were given an anesthetic agent maintained at a
  predetermined level (conc) for 15 minutes before making an incision. It
  was then noted whether the patient moved, i.e. jerked or twisted.

  This data frame contains the following columns:

  move
      a binary numeric vector coded for patient movement (0 = no movement,
      1 = movement)

  conc
      anesthetic concentration

  logconc
      logarithm of concentration

  nomove
      the complement of move

  unknown

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `anesthetic.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'anesthetic.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/anesthetic.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='anesthetic.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
