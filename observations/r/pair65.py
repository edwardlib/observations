# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pair65(path):
  """Heated Elastic Bands

  The `pair65` data frame has 9 rows and 2 columns. Eighteen elastic
  bands were divided into nine pairs, with bands of similar stretchiness
  placed in the same pair. One member of each pair was placed in hot water
  (60-65 degrees C) for four minutes, while the other was left at ambient
  temperature. After a wait of about ten minutes, the amounts of stretch,
  under a 1.35 kg weight, were recorded.

  This data frame contains the following columns:

  heated
      a numeric vector giving the stretch lengths for the heated bands

  ambient
      a numeric vector giving the stretch lengths for the unheated bands

  J.H. Maindonald

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pair65.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pair65.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/pair65.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pair65.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
