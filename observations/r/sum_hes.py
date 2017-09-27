# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sum_hes(path):
  """The Penn World Table, v. 5

  A panel of 125 observations from 1960 to 1985

  *total number of observations* : 3250

  *observation* : country

  *country* : World

  A data frame containing :

  year
      the year

  country
      the country name (factor)

  opec
      OPEC member?

  com
      communist regime?

  pop
      country's population (in thousands)

  gdp
      real GDP per capita (in 1985 US dollars)

  sr
      saving rate (in percent)

  Online supplements to Hayashi (2000).

  http://fhayashi.fc2web.com/datasets.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sum_hes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3250 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sum_hes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/plm/SumHes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sum_hes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
