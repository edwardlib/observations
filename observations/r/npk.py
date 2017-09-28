# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def npk(path):
  """Classical N, P, K Factorial Experiment

  A classical N, P, K (nitrogen, phosphate, potassium) factorial
  experiment on the growth of peas conducted on 6 blocks. Each half of a
  fractional factorial design confounding the NPK interaction was used on
  3 of the plots.

  The `npk` data frame has 24 rows and 5 columns:

  `block`
      which block (label 1 to 6).

  `N`
      indicator (0/1) for the application of nitrogen.

  `P`
      indicator (0/1) for the application of phosphate.

  `K`
      indicator (0/1) for the application of potassium.

  `yield`
      Yield of peas, in pounds/plot (the plots were (1/70) acre).

  Imperial College, London, M.Sc. exercise sheet.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `npk.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'npk.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/npk.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='npk.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
