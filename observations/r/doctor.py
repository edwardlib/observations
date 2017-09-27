# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def doctor(path):
  """Number of Doctor Visits

  a cross-section from 1986

  *number of observations* : 485

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  doctor
      the number of doctor visits

  children
      the number of children in the household

  access
      is a measure of access to health care

  health
      a measure of health status (larger positive numbers are associated
      with poorer health)

  Gurmu, Shiferaw (1997) “Semiparametric estimation of hurdle regression
  models with an application to medicaid utilization”, *Journal of Applied
  Econometrics*, **12(3)**, 225-242.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `doctor.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 485 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'doctor.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Doctor.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='doctor.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
