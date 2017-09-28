# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def primates(path):
  """Primate Body and Brain Weights

  A subset of `Animals` data frame from the MASS library. It contains
  the average body and brain measurements of five primates.

  This data frame contains the following columns:

  Bodywt
      a numeric vector consisting of the body weights (in kg) of five
      different primates

  Brainwt
      a numeric vector consisting of the corresponding brain weights (in
      g)

  P. J. Rousseeuw and A. M. Leroy (1987) Robust Regression and Outlier
  Detection. Wiley, p. 57.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `primates.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'primates.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/primates.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='primates.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
