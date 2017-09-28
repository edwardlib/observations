# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def british_unions(path):
  """BritishUnions

  Poll attitudes towards British trade unions

  A dataset with 17 observations on the following 7 variables.

  `Date`

  Month of the poll `Aug-77` to `Sep-79`

  `AgreePct`

  Percent who agree (unions have too much power)

  `DisagreePct`

  Percent who disagree

  `NetSupport`

  DisagreePct-AgreePct

  `Months`

  Months since August 1975

  `Late`

  `1`\ =after 1986 or `0`\ =before 1986

  `Unemployment`

  Unemployment rate

  | Data from the Ipsos MORI website at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `british_unions.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 17 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'british_unions.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/BritishUnions.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='british_unions.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
