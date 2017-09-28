# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def btrial(path):
  """data from Section 1.5

  The `btrial` data frame has 45 rows and 3 columns.

  This data frame contains the following columns:

  time
      Time to death or on-study time, months

  death
      Death indicator (0=alive, 1=dead)

  im
      Immunohistochemical response (1=negative, 2=positive)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Sedmak el al. Modern Pathology 2 (1989):
  516-520.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `btrial.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'btrial.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/btrial.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='btrial.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
