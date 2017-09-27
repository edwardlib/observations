# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def heights(path):
  """A data.frame of the Galton (1888) height and cubit data set.

  Francis Galton introduced the 'co-relation' in 1888 with a paper
  discussing how to measure the relationship between two variables. His
  primary example was the relationship between height and forearm length.
  The data table (`cubits`) is taken from Galton (1888). Unfortunately,
  there seem to be some errors in the original data table in that the
  marginal totals do not match the table.

  The data frame, `heights`, is converted from this table using
  `table2df`.

  A data frame with 348 observations on the following 2 variables.

  `height`
      Height in inches

  `cubit`
      Forearm length in inches

  Galton (1888)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `heights.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 348 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'heights.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/heights.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='heights.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
