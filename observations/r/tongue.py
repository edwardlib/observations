# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tongue(path):
  """data from Section 1.11

  The `tongue` data frame has 80 rows and 3 columns.

  This data frame contains the following columns:

  type
      Tumor DNA profile (1=Aneuploid Tumor, 2=Diploid Tumor)

  time
      Time to death or on-study time, weeks

  delta
      Death indicator (0=alive, 1=dead)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Sickle-Santanello et al. Cytometry 9
  (1988): 594-599.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tongue.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 80 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tongue.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/tongue.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tongue.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
