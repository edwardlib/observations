# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def austres(path):
  """Quarterly Time Series of the Number of Australian Residents

  Numbers (in thousands) of Australian residents measured quarterly from
  March 1971 to March 1994. The object is of class `"ts"`.

  P. J. Brockwell and R. A. Davis (1996) *Introduction to Time Series and

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `austres.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 89 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'austres.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/austres.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='austres.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
