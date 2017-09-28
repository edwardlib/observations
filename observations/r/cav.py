# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cav(path):
  """Position of Muscle Caveolae

  The `cav` data frame has 138 rows and 2 columns.

  The data gives the positions of the individual caveolae in a square
  region with sides of length 500 units. This grid was originally on a
  2.65mum square of muscle fibre. The data are those points falling in the
  lower left hand quarter of the region used for the dataset
  `caveolae.dat` in the spatial package by B.D. Ripley (1994).

  This data frame contains the following columns:

  `x`
      The x coordinate of the caveola's position in the region.

  `y`
      The y coordinate of the caveola's position in the region.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cav.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 138 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cav.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/cav.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cav.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
