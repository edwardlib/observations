# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def oddbooks(path):
  """Measurements on 12 books

  Data giving thickness (mm), height (cm), width (cm) and weight (g), of
  12 books. Books were selected so that thickness decreased as page area
  increased

  A data frame with 12 observations on the following 4 variables.

  thick
      a numeric vector

  height
      a numeric vector

  breadth
      a numeric vector

  weight
      a numeric vector

  JM took books from his library.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `oddbooks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'oddbooks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/oddbooks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='oddbooks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
