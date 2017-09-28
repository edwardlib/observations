# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def burt1(path):
  """11 emotional variables from Burt (1915)

  Cyril Burt reported an early factor analysis with a circumplex structure
  of 11 emotional variables in 1915. 8 of these were subsequently used by
  Harman in his text on factor analysis. Unfortunately, it seems as if
  Burt made a mistake for the matrix is not positive definite. With one
  change from .87 to .81 the matrix is positive definite.

  A correlation matrix based upon 172 "normal school age children aged
  9-12".

  Sociality
      Sociality

  Sorrow
      Sorrow

  Tenderness
      Tenderness

  Joy
      Joy

  Wonder
      Wonder

  Elation
      Elation

  Disgust
      Disgust

  Anger
      Anger

  Sex
      Sex

  Fear
      Fear

  Subjection
      Subjection

  (retrieved from the web at
  http://www.biodiversitylibrary.org/item/95822#790) Following a
  suggestion by Jan DeLeeuw.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `burt1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'burt1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/burt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='burt1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
