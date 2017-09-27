# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def seizure(path):
  """Epiliptic Seizures

  The `seizure` data frame has 59 rows and 7 columns. The dataset has
  the number of epiliptic seizures in each of four two-week intervals, and
  in a baseline eight-week inverval, for treatment and control groups with
  a total of 59 individuals.

  This data frame contains the following columns:

  y1
      the number of epiliptic seizures in the 1st 2-week interval

  y2
      the number of epiliptic seizures in the 2nd 2-week interval

  y3
      the number of epiliptic seizures in the 3rd 2-week interval

  y4
      the number of epiliptic seizures in the 4th 2-week interval

  trt
      an indicator of treatment

  base
      the number of epilitic seizures in a baseline 8-week interval

  age
      a numeric vector of subject age

  Thall, P.F. and Vail S.C. (1990) Some covariance models for longitudinal
  count data with overdispersion. *Biometrics* **46**: 657–671.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `seizure.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 59 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'seizure.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/geepack/seizure.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='seizure.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
