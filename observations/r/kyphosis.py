# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kyphosis(path):
  """Data on Children who have had Corrective Spinal Surgery

  The `kyphosis` data frame has 81 rows and 4 columns. representing data
  on children who have had corrective spinal surgery

  This data frame contains the following columns:

  `Kyphosis`
      a factor with levels `absent` `present` indicating if a kyphosis
      (a type of deformation) was present after the operation.

  `Age`
      in months

  `Number`
      the number of vertebrae involved

  `Start`
      the number of the first (topmost) vertebra operated on.

  John M. Chambers and Trevor J. Hastie eds. (1992) *Statistical Models in
  S*, Wadsworth and Brooks/Cole, Pacific Grove, CA.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kyphosis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 81 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kyphosis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/rpart/kyphosis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kyphosis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
