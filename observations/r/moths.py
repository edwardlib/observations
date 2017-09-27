# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def moths(path):
  """Moths Data

  The `moths` data frame has 41 rows and 4 columns. These data are from
  a study of the effect of habitat on the densities of two species of moth
  (A and P). Transects were set across the search area. Within transects,
  sections were identified according to habitat type.

  This data frame contains the following columns:

  meters
      length of transect

  A
      number of type A moths found

  P
      number of type P moths found

  habitat
      a factor with levels `Bank`, `Disturbed`, `Lowerside`,
      `NEsoak`, `NWsoak`, `SEsoak`, `SWsoak`, `Upperside`

  Sharyn Wragg, formerly of Australian National University

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `moths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 41 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'moths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/moths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='moths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
