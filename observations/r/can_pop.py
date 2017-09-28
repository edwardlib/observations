# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def can_pop(path):
  """Canadian Population Data

  The `CanPop` data frame has 16 rows and 2 columns. Decennial
  time-series of Canadian population, 1851–2001.

  This data frame contains the following columns:

  year
      census year.

  population
      Population, in millions

  Urquhart, M. C. and Buckley, K. A. H. (Eds.) (1965) *Historical
  Statistics of Canada*. Macmillan, p. 1369.

  Canada (1994) *Canada Year Book*. Statistics Canada, Table 3.2.

  Statistics Canada:
http://www12.statcan.ca/english/census01/products/standard/popdwell/Table-PR.
  cfm.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `can_pop.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'can_pop.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/CanPop.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='can_pop.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
