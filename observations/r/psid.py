# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def psid(path):
  """Panel Survey of Income Dynamics

  a cross-section from 1993

  *number of observations* : 4856

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  intnum
      1968 interview number

  persnum
      person number

  age
      age of individual

  educatn
      highest grade completed

  earnings
      total labor income

  hours
      annual work hours

  kids
      live births to this individual

  married
      last known marital status (married, never married, windowed,
      divorced, separated, NA/DF, no histories)

  Panel Survey of Income Dynamics.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `psid.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4856 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'psid.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/PSID.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='psid.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
