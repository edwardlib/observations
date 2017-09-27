# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def klein1(path):
  """Klein's Data on the U. S. Economy

  Data for Klein's (1950) simple econometric model of the U. S. economy.

  The `Klein` data frame has 22 rows and 10 columns.

  This data frame contains the following columns:

  Year
      1921–1941

  C
      consumption.

  P
      private profits.

  Wp
      private wages.

  I
      investment.

  K.lag
      capital stock, lagged one year.

  X
      equilibrium demand.

  Wg
      government wages.

  G
      government non-wage spending.

  T
      indirect business taxes and net exports.

  Greene, W. H. (1993) *Econometric Analysis, Second Edition.* Macmillan.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `klein1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'klein1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/sem/Klein.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='klein1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
