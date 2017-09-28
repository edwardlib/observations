# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def caschool(path):
  """The California Test Score Data Set

  a cross-section from 1998-1999

  *number of observations* : 420

  *observation* : schools

  *country* : United States

  A dataframe containing :

  distcod
      district code

  county
      county

  district
      district

  grspan
      grade span of district

  enrltot
      total enrollment

  teachers
      number of teachers

  calwpct
      percent qualifying for CalWorks

  mealpct
      percent qualifying for reduced-price lunch

  computer
      number of computers

  testscr
      average test score (read.scr+math.scr)/2

  compstu
      computer per student

  expnstu
      expenditure per student

  str
      student teacher ratio

  avginc
      district average income

  elpct
      percent of English learners

  readscr
      average reading score

  mathscr
      average math score

  California Department of Education http://www.cde.ca.gov.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `caschool.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 420 rows and 17 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'caschool.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Caschool.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='caschool.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
