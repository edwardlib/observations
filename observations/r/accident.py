# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def accident(path):
  """Ship Accidents

  a cross-section

  *number of observations* : 40

  A dataframe containing :

  type
      ship type, a factor with levels (A,B,C,D,E)

  constr
      year constructed, a factor with levels (C6064,C6569,C7074,C7579)

  operate
      year operated, a factor with levels (O6074,O7579)

  months
      measure of service amount

  acc
      accidents

  McCullagh, P. and J. Nelder (1983) *Generalized linear methods*, New
  York:Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `accident.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'accident.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Accident.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='accident.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
