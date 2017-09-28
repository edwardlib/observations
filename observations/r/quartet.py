# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def quartet(path):
  """Four Regression Datasets

  The `Quartet` data frame has 11 rows and 5 columns. These are
  contrived data.

  This data frame contains the following columns:

  x
      X-values for datasets 1–3.

  y1
      Y-values for dataset 1.

  y2
      Y-values for dataset 2.

  y3
      Y-values for dataset 3.

  x4
      X-values for dataset 4.

  y4
      Y-values for dataset 4.

  Anscombe, F. J. (1973) Graphs in statistical analysis. *American

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `quartet.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'quartet.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Quartet.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='quartet.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
