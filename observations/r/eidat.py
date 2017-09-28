# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def eidat(path):
  """Simulation Data for Ecological Inference

  This dataframe contains a simulated data set to illustrate the models
  for ecological inference.

  A table containing 4 variables ("t0", "t1", "x0", "x1") and 10

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `eidat.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'eidat.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/eidat.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='eidat.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
