# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cubits(path):
  """Galton's example of the relationship between height and 'cubit' or forearm
   length

  Francis Galton introduced the 'co-relation' in 1888 with a paper
  discussing how to measure the relationship between two variables. His
  primary example was the relationship between height and forearm length.
  The data table (cubits) is taken from Galton (1888). Unfortunately,
  there seem to be some errors in the original data table in that the
  marginal totals do not match the table.

  The data frame, `heights`, is converted from this table.

  A data frame with 9 observations on the following 8 variables.

  `16.5`
      Cubit length < 16.5

  `16.75`
      16.5 <= Cubit length < 17.0

  `17.25`
      17.0 <= Cubit length < 17.5

  `17.75`
      17.5 <= Cubit length < 18.0

  `18.25`
      18.0 <= Cubit length < 18.5

  `18.75`
      18.5 <= Cubit length < 19.0

  `19.25`
      19.0 <= Cubit length < 19.5

  `19.75`
      19.5 <= Cubit length

  Galton (1888)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cubits.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cubits.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/cubits.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cubits.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
