# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mcas(path):
  """The Massachusetts Test Score Data Set

  a cross-section from 1997-1998

  *number of observations* : 220

  *observation* : schools

  *country* : United States

  A dataframe containing :

  code
      district code (numerical)

  municipa
      municipality (name)

  district
      district name

  regday
      spending per pupil, regular

  specneed
      spending per pupil, special needs

  bilingua
      spending per pupil, bilingual

  occupday
      spending per pupil, occupational

  totday
      spending per pupil, total

  spc
      students per computer

  speced
      special education students

  lnchpct
      eligible for free or reduced price lunch

  tchratio
      students per teacher

  percap
      per capita income

  totsc4
      4th grade score (math+english+science)

  totsc8
      8th grade score (math+english+science)

  avgsalary
      average teacher salary

  pctel
      percent english learnersh

  Massachusetts Comprehensive Assessment System (MCAS), Massachusetts
  Department of Education, 1990 U.S. Census.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mcas.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 220 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mcas.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/MCAS.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mcas.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
