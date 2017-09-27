# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def elastic1(path):
  """Elastic Band Data Replicated

  The `elastic1` data frame has 7 rows and 2 columns giving, for each
  amount by which an elastic band is stretched over the end of a ruler,
  the distance that the band traveled when released.

  This data frame contains the following columns:

  stretch
      the amount by which the elastic band was stretched

  distance
      the distance traveled

  J. H. Maindonald

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `elastic1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'elastic1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/elastic1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='elastic1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
