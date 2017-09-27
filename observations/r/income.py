# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def income(path):
  """US family income from US census 2008

  US census data on family income from 2008

  A data frame with 44 observations on the following 4 variables.

  `value`
      lower boundary of the income group

  `count`
      Number of families within that income group

  `mean`
      Mean of the category

  `prop`
      proportion of families

  US Census: Table HINC-06. Income Distribution to $250,000 or More for
  Households: 2008

  http://www.census.gov/hhes/www/cpstables/032009/hhinc/new06\_000.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `income.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 44 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'income.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/income.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='income.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
