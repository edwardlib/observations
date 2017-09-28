# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def measles(path):
  """Deaths in London from measles

  Deaths in London from measles: 1629 – 1939, with gaps.

  The format is: Time-Series [1:311] from 1629 to 1939: 42 2 3 80 21 33 27
  12 NA NA ...

  Guy, W. A. 1882. Two hundred and fifty years of small pox in London.
  Journal of the Royal Statistical Society 399-443.

  Stocks, P. 1942. Measles and whooping cough during the dispersal of
  1939-1940. Journal of the Royal Statistical Society 105:259-291.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `measles.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 311 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'measles.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/measles.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='measles.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
