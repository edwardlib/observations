# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def allbacks(path):
  """Measurements on a Selection of Books

  The `allbacks` data frame gives measurements on the volume and weight
  of 15 books, some of which are softback (pb) and some of which are
  hardback (hb). Area of the hardback covers is also included.

  This data frame contains the following columns:

  volume
      book volumes in cubic centimeters

  area
      hard board cover areas in square centimeters

  weight
      book weights in grams

  cover
      a factor with levels `hb` hardback, `pb` paperback

  The bookshelf of J. H. Maindonald.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `allbacks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'allbacks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/allbacks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='allbacks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
