# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wool1(path):
  """Wool data

  This is a three-factor experiment with each factor at three levels, for
  a total of 27 runs. Samples of worsted yarn were with different levels
  of the three factors were given a cyclic load until the sample failed.
  The goal is to understand how cycles to failure depends on the factors.

  This data frame contains the following columns:

  len
      length of specimen (250, 300, 350 mm)

  amp
      amplitude of loading cycle (8, 9, 10 min)

  load
      load (40, 45, 50g)

  cycles
      number of cycles until failure

  Box, G. E. P. and Cox, D. R. (1964). An analysis of transformations
  (with discussion). *J. Royal Statist. Soc.*, B26, 211-46.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wool1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wool1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Wool.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wool1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
