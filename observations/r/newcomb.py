# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def newcomb(path):
  """Newcomb's Measurements of the Passage Time of Light

  A numeric vector giving the ‘Third Series’ of measurements of the
  passage time of light recorded by Newcomb in 1882. The given values
  divided by 1000 plus 24 give the time in millionths of a second for
  light to traverse a known distance. The ‘true’ value is now considered
  to be 33.02.

  S. M. Stigler (1973) Simon Newcomb, Percy Daniell, and the history of
  robust estimation 1885–1920. *Journal of the American Statistical
  Association* **68**, 872–879.

  R. G. Staudte and S. J. Sheather (1990) *Robust Estimation and Testing.*

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `newcomb.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 66 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'newcomb.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/newcomb.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='newcomb.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
