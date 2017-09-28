# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def moth_eggs(path):
  """Moth Eggs

  Body size and eggs produced for a species of moths

  A dataset with 39 observations on the following 2 variables.

  `BodyMass`

  Log of body size measured in grams

  `Eggs`

  Number of eggs present

  We thank Professor Itagaki and his students for sharing this data from

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `moth_eggs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 39 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'moth_eggs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/MothEggs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='moth_eggs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
