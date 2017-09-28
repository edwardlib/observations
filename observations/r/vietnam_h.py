# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def vietnam_h(path):
  """Medical Expenses in Viet–nam (household Level)

  a cross-section from 1997

  *number of observations* : 5999

  *observation* : households

  *country* : Vietnam

  A dataframe containing :

  sex
      gender of household head (male,female)

  age
      age of household head

  educyr
      schooling year of household head

  farm
      farm household ?

  urban
      urban household ?

  hhsize
      household size

  lntotal
      log household total expenditure

  lnmed
      log household medical expenditure

  lnrlfood
      log household food expenditure

  lnexp12m
      log of total household health care expenditure for 12 months

  commune
      commune

  Vietnam World Bank Livings Standards Survey.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `vietnam_h.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5999 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'vietnam_h.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/VietNamH.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='vietnam_h.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
