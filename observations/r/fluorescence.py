# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fluorescence(path):
  """Fluorescence

  Data from an experiment on calcium binding proteins

  A dataset with 51 observations on the following 2 variables.

  `Calcium`

  Log of free calcium concentration

  `ProteinProp`

  Proportion of protein bound to calcium

  Thanks to Suzanne Rohrback for providing these data from her honors

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fluorescence.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fluorescence.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Fluorescence.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fluorescence.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
