# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def twins(path):
  """data from Exercise 7.14, p225

  The `twins` data frame has 24 rows and 3 columns.

  This data frame contains the following columns:

  id
      Twin number

  age
      Age of twin's death from CHD, months

  death
      Death (male twin) from CHD indicator (1=dead from CHD, 0=alive or
      other cause of death)

  gender
      1=male, 2=female

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `twins.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'twins.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/twins.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='twins.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
