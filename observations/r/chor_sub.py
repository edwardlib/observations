# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chor_sub(path):
  """Subset of C-horizon of Kola Data

  This is a small rounded subset of the C-horizon data `chorizon` from
  package mvoutlier.

  A data frame with 61 observations on 10 variables. The variables contain
  scaled concentrations of chemical elements.

  Kola Project (1993-1998)

  See Also
  ~~~~~~~~

  `chorizon` in package mvoutlier and other Kola data in the same
  package.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chor_sub.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 61 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chor_sub.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/chorSub.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chor_sub.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
