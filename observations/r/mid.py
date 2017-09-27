# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mid(path):
  """Militarized Interstate Disputes

  A small sample from the militarized interstate disputes (MID) database.

  A table containing 6 variables ("conflict", "major", "contig", "power",
  "maxdem", "mindem", and "years") and 3,126 observations. For full
  variable descriptions, please see King and Zeng, 2001.

  Militarized Interstate Disputes database

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mid.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3126 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mid.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/mid.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mid.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
