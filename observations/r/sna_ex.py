# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sna_ex(path):
  """Simulated Example of Social Network Data

  This data set contains five sociomatrices of simulated data social
  network data.

  Each variable in the dataset is a 25 by 25 matrix of simulated social
  network data. The matrices are labeled "Var1", "Var2", "Var3", "Var4",
  and "Var5".


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sna_ex.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 0 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sna_ex.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/sna.ex.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sna_ex.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
