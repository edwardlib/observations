# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def uspop(path):
  """Populations Recorded by the US Census

  This data set gives the population of the United States (in millions) as
  recorded by the decennial census for the period 1790–1970.

  A time series of 19 values.

  McNeil, D. R. (1977) *Interactive Data Analysis*. New York: Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `uspop.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 19 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'uspop.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/uspop.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='uspop.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
