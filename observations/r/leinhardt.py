# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leinhardt(path):
  """Data on Infant-Mortality

  The `Leinhardt` data frame has 105 rows and 4 columns. The
  observations are nations of the world around 1970.

  This data frame contains the following columns:

  income
      Per-capita income in U. S. dollars.

  infant
      Infant-mortality rate per 1000 live births.

  region
      A factor with levels: `Africa`; `Americas`; `Asia`, Asia and
      Oceania; `Europe`.

  oil
      Oil-exporting country. A factor with levels: `no`, `yes`.

  Leinhardt, S. and Wasserman, S. S. (1979) Exploratory data analysis: An
  introduction to selected methods. In Schuessler, K. (Ed.) *Sociological
  Methodology 1979* Jossey-Bass.

  *The New York Times*, 28 September 1975, p. E-3, Table 3.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leinhardt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 105 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leinhardt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Leinhardt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leinhardt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
