# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def mroz1(path):
  """Labor Supply Data

  a cross-section

  *number of observations* : 753

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  work
      participation in 1975 ?

  hoursw
      wife's hours of work in 1975

  child6
      number of children less than 6 years old in household

  child618
      number of children between ages 6 and 18 in household

  agew
      wife's age

  educw
      wife's educational attainment, in years

  hearnw
      wife's average hourly earnings, in 1975 dollars

  wagew
      wife's wage reported at the time of the 1976 interview (not= 1975
      estimated wage)

  hoursh
      husband's hours worked in 1975

  ageh
      husband's age

  educh
      husband's educational attainment, in years

  wageh
      husband's wage, in 1975 dollars

  income
      family income, in 1975 dollars

  educwm
      wife's mother's educational attainment, in years

  educwf
      wife's father's educational attainment, in years

  unemprate
      unemployment rate in county of residence, in percentage points

  city
      lives in large city (SMSA) ?

  experience
      actual years of wife's previous labor market experience

  Mroz, T. (1987) “The sensitivity of an empirical model of married
  women's hours of work to economic and statistical assumptions”,
  *Econometrica*, **55**, 765-799.

  1976 Panel Study of Income Dynamics.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `mroz1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 753 rows and 18 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'mroz1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Mroz.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='mroz1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
