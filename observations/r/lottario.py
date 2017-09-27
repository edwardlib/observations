# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lottario(path):
  """Ontario Lottery Data

  The data frame `Lottario` is a summary of 122 weekly draws of an
  Ontario lottery, beginning in November, 1978. Each draw consists of 7
  numbered balls, drawn without replacement from an urn consisting of
  balls numbered from 1 through 39.

  This data frame contains the following columns:

  Number
      the integers from 1 to 39, representing the numbered balls

  Frequency
      the number of occurrences of each numbered ball

  The Ontario Lottery Corporation

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lottario.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 39 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lottario.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/Lottario.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lottario.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
