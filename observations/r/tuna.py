# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tuna(path):
  """Tuna Sighting Data

  The `tuna` data frame has 64 rows and 1 columns.

  The data come from an aerial line transect survey of Southern Bluefin
  Tuna in the Great Australian Bight. An aircraft with two spotters on
  board flies randomly allocated line transects. Each school of tuna
  sighted is counted and its perpendicular distance from the transect
  measured. The survey was conducted in summer when tuna tend to stay on
  the surface.

  This data frame contains the following column:

  `y`
      The perpendicular distance, in miles, from the transect for 64
      independent sightings of tuna schools.

  The data were obtained from

  Chen, S.X. (1996) Empirical likelihood confidence intervals for
  nonparametric density estimation. *Biometrika*, **83**, 329–341.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tuna.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 64 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tuna.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/tuna.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tuna.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
