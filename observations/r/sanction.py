# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sanction(path):
  """Multilateral Economic Sanctions

  Data on bilateral sanctions behavior for selected years during the
  general period 1939-1983. This data contains errors that have since been
  corrected. Please contact Lisa Martin before using this data for
  publication.

  A table containing 8 variables ("mil", "coop", "target", "import",
  "export", "cost", "num", and "ncost") and 78 observations. For full
  variable description, see Martin, 1992.

  Martin, 1992

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sanction.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 78 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sanction.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/sanction.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sanction.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
