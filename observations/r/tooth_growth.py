# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tooth_growth(path):
  """The Effect of Vitamin C on Tooth Growth in Guinea Pigs

  The response is the length of odontoblasts (cells responsible for tooth
  growth) in 60 guinea pigs. Each animal received one of three dose levels
  of vitamin C (0.5, 1, and 2 mg/day) by one of two delivery methods,
  (orange juice or ascorbic acid (a form of vitamin C and coded as
  `VC`).

  A data frame with 60 observations on 3 variables.

  +--------+--------+-----------+-------------------------------+
  | [,1]   | len    | numeric   | Tooth length                  |
  +--------+--------+-----------+-------------------------------+
  | [,2]   | supp   | factor    | Supplement type (VC or OJ).   |
  +--------+--------+-----------+-------------------------------+
  | [,3]   | dose   | numeric   | Dose in milligrams/day        |
  +--------+--------+-----------+-------------------------------+

  C. I. Bliss (1952) *The Statistics of Bioassay*. Academic Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tooth_growth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tooth_growth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/ToothGrowth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tooth_growth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
