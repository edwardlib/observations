# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def animals(path):
  """Attributes of Animals

  This data set considers 6 binary attributes for 20 animals.

  A data frame with 20 observations on 6 variables:

  [ , 1]

  war

  warm-blooded

  [ , 2]

  fly

  can fly

  [ , 3]

  ver

  vertebrate

  [ , 4]

  end

  endangered

  [ , 5]

  gro

  live in groups

  [ , 6]

  hai

  have hair

  All variables are encoded as 1 = ‘no’, 2 = ‘yes’.

  Leonard Kaufman and Peter J. Rousseeuw (1990): *Finding Groups in Data*
  (pp 297ff). New York: Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `animals.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'animals.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/animals.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='animals.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
