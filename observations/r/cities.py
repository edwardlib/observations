# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cities(path):
  """Populations of Major Canadian Cities (1992-96)

  Population estimates for several Canadian cities.

  This data frame contains the following columns:

  CITY
      a factor, consisting of the city names

  REGION
      a factor with 5 levels (ATL=Atlantic, ON=Ontario, QC=Quebec,
      PR=Prairies, WEST=Alberta and British Columbia) representing the
      location of the cities

  POP1992
      a numeric vector giving population in 1000's for 1992

  POP1993
      a numeric vector giving population in 1000's for 1993

  POP1994
      a numeric vector giving population in 1000's for 1994

  POP1995
      a numeric vector giving population in 1000's for 1995

  POP1996
      a numeric vector giving population in 1000's for 1996

  Statistics Canada

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cities.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cities.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/cities.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cities.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
