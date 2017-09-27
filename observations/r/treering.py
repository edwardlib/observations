# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def treering(path):
  """Yearly Treering Data, -6000–1979

  Contains normalized tree-ring widths in dimensionless units.

  A univariate time series with 7981 observations. The object is of class
  `"ts"`.

  Each tree ring corresponds to one year.

  Time Series Data Library:
  http://www-personal.buseco.monash.edu.au/~hyndman/TSDL/, series
  ‘CA535.DAT’

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `treering.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7980 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'treering.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/treering.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='treering.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
