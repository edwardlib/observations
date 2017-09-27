# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hodg(path):
  """data from Section 1.10

  The `hodg` data frame has 43 rows and 6 columns.

  This data frame contains the following columns:

  gtype
      Graft type (1=allogenic, 2=autologous)

  dtype
      Disease type (1=Non Hodgkin lymphoma, 2=Hodgkins disease)

  time
      Time to death or relapse, days

  delta
      Death/relapse indicator (0=alive, 1=dead)

  score
      Karnofsky score

  wtime
      Waiting time to transplant in months

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. Avalos et al. Bone Marrow Transplantation
  13(1993):133-138.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hodg.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 43 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hodg.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/hodg.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hodg.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
