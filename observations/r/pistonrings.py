# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pistonrings(path):
  """Piston Rings Failures

  Number of failures of piston rings in three legs of four steam-driven
  compressors.

  A two-way classification, see `table`.

  S. J. Haberman (1973), The analysis of residuals in cross-classificed
  tables. *Biometrics* **29**, 205–220.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pistonrings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pistonrings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/HSAUR/pistonrings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pistonrings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
