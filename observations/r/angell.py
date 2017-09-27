# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def angell(path):
  """Moral Integration of American Cities

  The `Angell` data frame has 43 rows and 4 columns. The observations
  are 43 U. S. cities around 1950.

  This data frame contains the following columns:

  moral
      Moral Integration: Composite of crime rate and welfare expenditures.

  hetero
      Ethnic Heterogenity: From percentages of nonwhite and foreign-born
      white residents.

  mobility
      Geographic Mobility: From percentages of residents moving into and
      out of the city.

  region
      A factor with levels: `E` Northeast; `MW` Midwest; `S`
      Southeast; `W` West.

  Angell, R. C. (1951) The moral integration of American Cities. *American
  Journal of Sociology* **57** (part 2), 1–140.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `angell.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 43 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'angell.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Angell.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='angell.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
