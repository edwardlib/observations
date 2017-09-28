# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def strike_nb(path):
  """Number of Strikes in Us Manufacturing

  monthly observations from 1968(1) to 1976 (12)

  *number of observations* : 108

  *observation* : country

  *country* : United States

  A time serie containing :

  strikes
      number of strikes (number of contract strikes in U.S. manufacturing
      beginning each month)

  output
      level of economic activity (measured as cyclical departure of
      aggregate production from its trend level)

  time
      a time trend from 1 to 108

  Kennan, J. (1985) “The Duration of Contract strikes in U.S.
  Manufacturing”, *Journal of Econometrics*, **28**, 5-28.

  Cameron, A.C. and Trivedi P.K. (1990) “Regression Based Tests for
  Overdispersion in the Poisson Model”, *Journal of Econometrics*,
  december, 347-364.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `strike_nb.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 108 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'strike_nb.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/StrikeNb.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='strike_nb.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
