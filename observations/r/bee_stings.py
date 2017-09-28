# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bee_stings(path):
  """BeeStings

  Does number of beestings depend on previous stings?

  A dataset with 18 observations on the following 3 variables.

  `Occasion`

  Trial: I to IX

  `Treatment`

  `Fresh` or `Stung`

  `Stingers`

  Number of stingers

  Free, J.B. (1961) "The stinging response of honeybees," Animal Behavior,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bee_stings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bee_stings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/BeeStings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bee_stings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
