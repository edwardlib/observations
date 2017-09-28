# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vietnam_i(path):
  """Medical Expenses in Viet–nam (individual Level)

  a cross-section from 1997

  *number of observations* : 27765

  *observation* : individuals

  *country* : Vietnam

  A dataframe containing :

  pharvis
      number of direct pharmacy visits

  lnhhexp
      log of total medical expenditure

  age
      age of household head

  sex
      gender (male,female)

  married
      married ?

  educ
      completed diploma level ?

  illness
      number of of illnesses experiences in past 12 months

  injury
      injured during survey period ?

  illdays
      number of illness days

  actdays
      number of days of limited activity

  insurance
      respondent has health insurance coverage ?

  commune
      commune

  Vietnam World Bank Livings Standards Survey.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vietnam_i.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27765 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vietnam_i.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/VietNamI.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vietnam_i.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
