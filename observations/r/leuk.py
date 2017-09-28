# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leuk(path):
  """Survival Times and White Blood Counts for Leukaemia Patients

  A data frame of data from 33 leukaemia patients.

  A data frame with columns:

  `wbc`
      white blood count.

  `ag`
      a test result, `"present"` or `"absent"`.

  `time`
      survival time in weeks.

  Cox, D. R. and Oakes, D. (1984) *Analysis of Survival Data*. Chapman &
  Hall, p. 9.

  Taken from

  Feigl, P. & Zelen, M. (1965) Estimation of exponential survival
  probabilities with concomitant information. *Biometrics* **21**,
  826–838.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leuk.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 33 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leuk.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/leuk.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leuk.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
