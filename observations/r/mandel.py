# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mandel(path):
  """Contrived Collinear Data

  The `Mandel` data frame has 8 rows and 3 columns.

  This data frame contains the following columns:

  x1
      first predictor.

  x2
      second predictor.

  y
      response.

  Mandel, J. (1982) Use of the singular value decomposition in regression
  analysis. *The American Statistician* **36**, 15–24.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mandel.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mandel.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Mandel.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mandel.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
