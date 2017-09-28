# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ohio(path):
  """Ohio Children Wheeze Status

  The `ohio` data frame has 2148 rows and 4 columns. The dataset is a
  subset of the six-city study, a longitudinal study of the health effects
  of air pollution.

  This data frame contains the following columns:

  resp
      an indicator of wheeze status (1=yes, 0=no)

  id
      a numeric vector for subject id

  age
      a numeric vector of age, 0 is 9 years old

  smoke
      an indicator of maternal smoking at the first year of the study

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ohio.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2148 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ohio.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/geepack/ohio.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ohio.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
