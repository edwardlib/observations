# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sahlins(path):
  """Agricultural Production in Mazulu Village

  The `Sahlins` data frame has 20 rows and 2 columns. The observations
  are households in a Central African village.

  This data frame contains the following columns:

  consumers
      Consumers/Gardener, ratio of consumers to productive individuals.

  acres
      Acres/Gardener, amount of land cultivated per gardener.

  Sahlins, M. (1972) *Stone Age Economics.* Aldine [Table 3.1].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sahlins.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sahlins.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Sahlins.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sahlins.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
