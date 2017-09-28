# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def va_lung_cancer(path):
  """Veteran's Administration Lung Cancer Trial

  Veteran's Administration lung cancer trial from Kalbfleisch & Prentice.

  A data frame with columns:

  `stime`
      survival or follow-up time in days.

  `status`
      dead or censored.

  `treat`
      treatment: standard or test.

  `age`
      patient's age in years.

  `Karn`
      Karnofsky score of patient's performance on a scale of 0 to 100.

  `diag.time`
      times since diagnosis in months at entry to trial.

  `cell`
      one of four cell types.

  `prior`
      prior therapy?

  Kalbfleisch, J.D. and Prentice R.L. (1980) *The Statistical Analysis of
  Failure Time Data.* Wiley.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `va_lung_cancer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 137 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'va_lung_cancer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/VA.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='va_lung_cancer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
