# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nursing(path):
  """Nursing

  Characteristics of nursing homes in New Mexico.

  A dataset with 52 observations on the following 7 variables.

  `Beds`

  Number of beds in the nursing home

  `InPatientDays`

  Annual medical in-patient days (in hundreds)

  `AllPatientDays`

  Annual total patient days (in hundreds)

  `PatientRevenue`

  Annual patinet care revenue (in hundreds of dollars)

  `NurseSalaries`

  Annual nursing salaries (in hundreds of dollars)

  `FacilitiesExpend`

  Annual facilities expenditure (in hundreds of dollars)

  `Rural`

  1=\ `rural` or 0=\ `non-rural`

  Downloaded from DASL at
  http://lib.stat.cmu.edu/DASL/Datafiles/Nursingdat.html

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nursing.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 52 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nursing.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Nursing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nursing.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
