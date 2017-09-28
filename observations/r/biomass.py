# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def biomass(path):
  """Biomass Data

  The `biomass` data frame has 135 rows and 8 columns. The
  `rainforest` data frame is a subset of this one.

  This data frame contains the following columns:

  dbh
      a numeric vector

  wood
      a numeric vector

  bark
      a numeric vector

  fac26
      a factor with 3 levels

  root
      a numeric vector

  rootsk
      a numeric vector

  branch
      a numeric vector

  species
      a factor with levels `Acacia mabellae`, `C. fraseri`,
      `Acmena smithii`, `B. myrtifolia`

  J. Ash, Australian National University

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `biomass.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 153 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'biomass.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/biomass.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='biomass.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
