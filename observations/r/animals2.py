# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def animals2(path):
  """Brain and Body Weights for 65 Species of Land Animals

  A data frame with average brain and body weights for 62 species of land
  mammals and three others.

  Note that this is simply the union of `Animals` and `mammals`.

  `body`
      body weight in kg

  `brain`
      brain weight in g

  Weisberg, S. (1985) *Applied Linear Regression.* 2nd edition. Wiley, pp.
  144–5.

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection.* Wiley, p. 57.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `animals2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 65 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'animals2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/robustbase/Animals2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='animals2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
