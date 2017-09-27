# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def federalist(path):
  """‘May’ in Federalist Papers

  Data from Mosteller & Wallace (1984) investigating the use of certain
  keywords (‘may’ in this data set) to identify the author of 12 disputed
  ‘Federalist Papers’ by Alexander Hamilton, John Jay and James Madison.

  A 1-way table giving the number of occurrences of ‘may’ in 262 blocks of
  text. The variable and its levels are

  No

  Name

  Levels

  1

  nMay

  0, 1, ..., 6

  Michael Friendly (2000), Visualizing Categorical Data, page 19.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `federalist.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'federalist.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Federalist.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='federalist.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
