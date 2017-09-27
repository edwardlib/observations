# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rats(path):
  """Rat treatment data from Mantel et al

  Rat treatment data from Mantel et al. Three rats were chosen from each
  of 100 litters, one of which was treated with a drug, and then all
  followed for tumor incidence.

  +-----------+----------------------------------------+
  | litter:   | litter number from 1 to 100            |
  +-----------+----------------------------------------+
  | rx:       | treatment,(1=drug, 0=control)          |
  +-----------+----------------------------------------+
  | time:     | time to tumor or last follow-up        |
  +-----------+----------------------------------------+
  | status:   | event status, 1=tumor and 0=censored   |
  +-----------+----------------------------------------+
  | sex:      | male or female                         |
  +-----------+----------------------------------------+

  N. Mantel, N. R. Bohidar and J. L. Ciminera. Mantel-Haenszel analyses of
  litter-matched time to response data, with modifications for recovery of
  interlitter information. Cancer Research, 37:3863-3868, 1977.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rats.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 300 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rats.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/rats.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rats.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
