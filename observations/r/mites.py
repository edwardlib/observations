# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mites(path):
  """Mites and Wilt Disease

  Data from an experiment to test whether exposure to mites protects
  against Wilt Disease in cotton plants.

  A data frame with 47 observations on the following variables.

  -  `treatment` a factor with levels `mites` and `no mites`

  -  `outcome` a factor with levels `wilt` and `no wilt`

  Statistics for the Life Sciences, Third Edition; Myra Samuels & Jeffrey
  Witmer (2003), page 409.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mites.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 47 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mites.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Mites.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mites.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
