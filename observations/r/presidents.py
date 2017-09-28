# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def presidents(path):
  """Quarterly Approval Ratings of US Presidents

  The (approximately) quarterly approval rating for the President of the
  United States from the first quarter of 1945 to the last quarter of
  1974.

  A time series of 120 values.

  The Gallup Organisation.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `presidents.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 120 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'presidents.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/presidents.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='presidents.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
