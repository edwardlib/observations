# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def somerville(path):
  """Visits to Lake Somerville

  a cross-section from 1980

  *number of observations* : 659

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  visits
      annual number of visits to lake Somerville

  quality
      quality ranking score for lake Somerville

  ski
      engaged in water–skiing at the lake ?

  income
      annual household income

  feeSom
      annual user fee paid at lake Somerville ?

  costCon
      expenditures when visiting lake Conroe

  costSom
      expenditures when visiting lake Somerville

  costHoust
      expenditures when visiting lake Houston

  Seller, Christine, John R. Stoll and Jean–Paul Chavas (1985) “Valuation
  of empirical measures of welfare change : a comparison of nonmarket
  techniques”, *Land Economics*, **61(2)**, may, 156–175.

  Gurmu, Shiferaw and Pravin K. Trivedi (1996) “ Excess zeros in count
  models for recreational trips”, *Journal of Business and Economics
  Statistics*, **14(4)**, october, 469–477.

  Santos Silva, Jao M. C. (2001) “A score test for non–nested hypotheses
  with applications to discrete data models”, *Journal of Applied
  Econometrics*, **16(5)**, 577–597.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `somerville.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 659 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'somerville.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Somerville.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='somerville.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
