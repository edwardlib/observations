# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def skye(path):
  """AFM Compositions of Aphyric Skye Lavas

  The `Skye` data frame has 23 rows and 3 columns.

  This data frame contains the following columns:

  `A`
      Percentage of sodium and potassium oxides.

  `F`
      Percentage of iron oxide.

  `M`
      Percentage of magnesium oxide.

  R. N. Thompson, J. Esson and A. C. Duncan (1972) Major element chemical
  variation in the Eocene lavas of the Isle of Skye. *J. Petrology*,
  **13**, 219–253.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `skye.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'skye.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/Skye.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='skye.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
