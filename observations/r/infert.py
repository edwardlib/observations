# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def infert(path):
  """Infertility after Spontaneous and Induced Abortion

  This is a matched case-control study dating from before the availability
  of conditional logistic regression.

+---------------------+--------------------------+--------------------------+
| 1.                  | Education                | 0 = 0-5 years            |
+---------------------+--------------------------+--------------------------+
|                     |                          | 1 = 6-11 years           |
+---------------------+--------------------------+--------------------------+
|                     |                          | 2 = 12+ years            |
+---------------------+--------------------------+--------------------------+
| 2.                  | age                      | age in years of case     |
+---------------------+--------------------------+--------------------------+
| 3.                  | parity                   | count                    |
+---------------------+--------------------------+--------------------------+
| 4.                  | number of prior          | 0 = 0                    |
+---------------------+--------------------------+--------------------------+
|                     | induced abortions        | 1 = 1                    |
+---------------------+--------------------------+--------------------------+
|                     |                          | 2 = 2 or more            |
+---------------------+--------------------------+--------------------------+
| 5.                  | case status              | 1 = case                 |
+---------------------+--------------------------+--------------------------+
|                     |                          | 0 = control              |
+---------------------+--------------------------+--------------------------+
| 6.                  | number of prior          | 0 = 0                    |
+---------------------+--------------------------+--------------------------+
|                     | spontaneous abortions    | 1 = 1                    |
+---------------------+--------------------------+--------------------------+
|                     |                          | 2 = 2 or more            |
+---------------------+--------------------------+--------------------------+
| 7.                  | matched set number       | 1-83                     |
+---------------------+--------------------------+--------------------------+
| 8.                  | stratum number           | 1-63                     |
+---------------------+--------------------------+--------------------------+

  Trichopoulos *et al* (1976) *Br. J. of Obst. and Gynaec.* **83**,
  645–650.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `infert.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 248 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'infert.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/infert.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='infert.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
