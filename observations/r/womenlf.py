# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def womenlf(path):
  """Canadian Women's Labour-Force Participation

  The `Womenlf` data frame has 263 rows and 4 columns. The data are from
  a 1977 survey of the Canadian population.

  This data frame contains the following columns:

  partic
      Labour-Force Participation. A factor with levels (note: out of
      order): `fulltime`, Working full-time; `not.work`, Not working
      outside the home; `parttime`, Working part-time.

  hincome
      Husband's income, $1000s.

  children
      Presence of children in the household. A factor with levels:
      `absent`, `present`.

  region
      A factor with levels: `Atlantic`, Atlantic Canada; `BC`, British
      Columbia; `Ontario`; `Prairie`, Prairie provinces; `Quebec`.

  *Social Change in Canada Project.* York Institute for Social Research.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `womenlf.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 263 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'womenlf.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Womenlf.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='womenlf.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
