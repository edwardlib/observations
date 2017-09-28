# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def university(path):
  """Provision of University Teaching and Research

  a cross-section from 1988

  *number of observations* : 62

  *observation* : schools

  *country* : United Kingdown

  A dataframe containing :

  undstudents
      undergraduate students

  poststudents
      postgraduate students

  nassets
      net assets

  acnumbers
      academic numbers

  acrelnum
      academic related numbers

  clernum
      clerical numbers

  compop
      computer operators

  techn
      technicians

  stfees
      student fees

  acpay
      academic pay

  acrelpay
      academic related pay

  secrpay
      secretarial pay

  admpay
      admin pay

  agresrk
      aggregate research rank

  furneq
      furniture and equipment

  landbuild
      land and buildings

  resgr
      research grants

  Glass, J.C., D.G. McKillop and N. Hyndman (1995) “Efficiency in the
  provision of university teaching and research : an empirical analysis of
  UK universities”, *Journal of Applied Econometrics*, **10(1)**,
  january–march, 61–72.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `university.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 62 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'university.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/University.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='university.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
