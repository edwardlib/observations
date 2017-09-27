# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cloth(path):
  """Number of Flaws in Cloth

  The `cloth` data frame has 32 rows and 2 columns.

  This data frame contains the following columns:

  `x`
      The length of the roll of cloth.

  `y`
      The number of flaws found in the roll.

  The data were obtained from

  Bissell, A.F. (1972) A negative binomial model with varying element
  size. *Biometrika*, **59**, 435–441.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cloth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 32 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cloth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/cloth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cloth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
