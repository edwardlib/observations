# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def alfalfa(path):
  """Alfalfa

  Growth of alfalfa sprouts in acidic conditions

  A dataset with 15 observations on the following 3 variables.

  `Ht4`

  Height of alfalfa sprouts after four days

  `Acid`

  Amount of acid: `1.5HCl`, `3.0HCl`, or `water`

  `Row`

  `a`\ = closest to window through `e`\ =farthest from window

  Neumann, A., Richards, A.-L., and Randa, J. (2001). Effects of acid rain
  on alfalfa plants. Unpublished manuscript, Oberlin College.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `alfalfa.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'alfalfa.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Alfalfa.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='alfalfa.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
