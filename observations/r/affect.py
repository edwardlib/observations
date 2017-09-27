# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def affect(path):
  """Two data sets of affect and arousal scores as a function of personality an
  d movie conditions

  A recurring question in the study of affect is the proper dimensionality
  and the relationship to various personality dimensions. Here is a data
  set taken from two studies of mood and arousal using movies to induce
  affective states.

  Data collected at the Personality, Motivation, and Cognition Laboratory,
  Northwestern University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `affect.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 330 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'affect.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/affect.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='affect.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
