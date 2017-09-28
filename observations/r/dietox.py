# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def dietox(path):
  """Growth curves of pigs in a 3x3 factorial experiment

  The `dietox` data frame has 861 rows and 7 columns.

  This data frame contains the following columns:

  Weight
      a numeric vector

  Feed
      a numeric vector

  Time
      a numeric vector

  Pig
      a numeric vector

  Evit
      a numeric vector

  Cu
      a numeric vector

  Litter
      a numeric vector

  Lauridsen, C., Højsgaard, S.,Sørensen, M.T. C. (1999) Influence of
  Dietary Rapeseed Oli, Vitamin E, and Copper on Performance and
  Antioxidant and Oxidative Status of Pigs. J. Anim. Sci.77:906-916

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `dietox.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 861 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'dietox.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/geepack/dietox.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='dietox.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
