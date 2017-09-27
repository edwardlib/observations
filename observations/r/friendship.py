# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def friendship(path):
  """Simulated Example of Schoolchildren Friendship Network

  This data set contains six sociomatrices of simulated data on friendship
  ties among schoolchildren.

  Each variable in the dataset is a 15 by 15 matrix representing some form
  of social network tie held by the fictitious children. The matrices are
  labeled "friends", "advice", "prestige", "authority", "perpower" and
  "per".

  The sociomatrices were combined into the friendship dataset using the
  format.network.data function from the netglm package by Skyler Cranmer
  as shown in the example.

  fictitious

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `friendship.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 0 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'friendship.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/friendship.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='friendship.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
