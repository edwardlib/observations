# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bfeed(path):
  """data from Section 1.14

  The `bfeed` data frame has 927 rows and 10 columns.

  This data frame contains the following columns:

  duration
      Duration of breast feeding, weeks

  delta
      Indicator of completed breast feeding (1=yes, 0=no)

  race
      Race of mother (1=white, 2=black, 3=other)

  poverty
      Mother in poverty (1=yes, 0=no)

  smoke
      Mother smoked at birth of child (1=yes, 0=no)

  alcohol
      Mother used alcohol at birth of child (1=yes, 0=no)

  agemth
      Age of mother at birth of child

  ybirth
      Year of birth

  yschool
      Education level of mother (years of school)

  pc3mth
      Prenatal care after 3rd month (1=yes, 0=no)

  Klein and Moeschberger (1997) *Survival Analysis Techniques for Censored
  and truncated data*, Springer. *National Longitudinal Survey of Youth
  Handbook* The Ohio State University, 1995.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bfeed.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 927 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bfeed.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/KMsurv/bfeed.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bfeed.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
