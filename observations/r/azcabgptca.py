# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def azcabgptca(path):
  """azcabgptca

  Random subset of the 1991 Arizona Medicare data for patients
  hospitalized subsequent to undergoing a CABG (DRGs 106, 107) or PTCA
  (DRG 112) cardiovascular procedure.

  A data frame with 1959 observations on the following 6 variables.

  `died`
      systolic blood pressure of subject

  `procedure`
      1=CABG; 0=PTCA

  `gender`
      1=male; 0=female

  `age`
      age of subject

  `los`
      hospital length of stay

  `type`
      1=emerg/urgent; 0=elective

  Hilbe, Negative Binomial Regression, 2nd ed, Cambridge Univ Press

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `azcabgptca.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1959 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'azcabgptca.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/azcabgptca.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='azcabgptca.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
