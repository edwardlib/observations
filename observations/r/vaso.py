# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vaso(path):
  """Vaso Constriction Skin Data Set

  Finney's data on vaso constriction in the skin of the digits.

  A data frame with 39 observations on the following 3 variables.

  `Volume`
      Inhaled volume of air

  `Rate`
      Rate of inhalation

  `Y`
      vector of 0 or 1 values.

  Finney, D.J. (1947) The estimation from individual records of the
  relationship between dose and quantal response. *Biometrika* **34**,
  320–334

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vaso.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 39 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vaso.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/vaso.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vaso.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
