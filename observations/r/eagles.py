# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def eagles(path):
  """Foraging Ecology of Bald Eagles

  Knight and Skagen collected during a field study on the foraging
  behaviour of wintering Bald Eagles in Washington State, USA data
  concerning 160 attempts by one (pirating) Bald Eagle to steal a chum
  salmon from another (feeding) Bald Eagle.

  The `eagles` data frame has 8 rows and 5 columns.

  `y`
      Number of successful attempts.

  `n`
      Total number of attempts.

  `P`
      Size of pirating eagle (`L` = large, `S` = small).

  `A`
      Age of pirating eagle (`I` = immature, `A` = adult).

  `V`
      Size of victim eagle (`L` = large, `S` = small).

  Knight, R. L. and Skagen, S. K. (1988) Agonistic asymmetries and the
  foraging ecology of Bald Eagles. *Ecology* **69**, 1188–1194.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `eagles.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'eagles.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/eagles.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='eagles.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
