# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hi_hours_worked(path):
  """Health Insurance and Hours Worked By Wives

  a cross-section from 1993

  *number of observations* : 22272

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  whrswk
      hours worked per week by wife

  hhi
      wife covered by husband's HI ?

  whi
      wife has HI thru her job ?

  hhi2
      husband has HI thru own job ?

  education
      a factor with levels, "<9years", "9-11years", "12years",
      "13-15years", "16years", ">16years"

  race
      one of white, black, other

  hispanic
      hispanic ?

  experience
      years of potential work experience

  kidslt6
      number of kids under age of 6

  kids618
      number of kids 6–18 years old

  husby
      husband's income in thousands of dollars

  region
      one of other, northcentral, south, west

  wght
      sampling weight

  Olson, Craig A. (1998) “A comparison of parametric and semiparametric
  estimates of the effect of spousal health insurance coverage on weekly
  hours worked by wiwes”, *Journal of Applied Econometrics*, **13(5)**,
  september–october, 543–565.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hi_hours_worked.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 22272 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hi_hours_worked.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/HI.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hi_hours_worked.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
