# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def topo(path):
  """Spatial Topographic Data

  The `topo` data frame has 52 rows and 3 columns, of topographic
  heights within a 310 feet square.

  This data frame contains the following columns:

  `x`
      x coordinates (units of 50 feet)

  `y`
      y coordinates (units of 50 feet)

  `z`
      heights (feet)

  Davis, J.C. (1973) *Statistics and Data Analysis in Geology.* Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `topo.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 52 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'topo.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/topo.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='topo.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
