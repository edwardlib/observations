# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ericksen(path):
  """The 1980 U.S. Census Undercount

  The `Ericksen` data frame has 66 rows and 9 columns. The observations
  are 16 large cities, the remaining parts of the states in which these
  cities are located, and the other U. S. states.

  This data frame contains the following columns:

  minority
      Percentage black or Hispanic.

  crime
      Rate of serious crimes per 1000 population.

  poverty
      Percentage poor.

  language
      Percentage having difficulty speaking or writing English.

  highschool
      Percentage age 25 or older who had not finished highschool.

  housing
      Percentage of housing in small, multiunit buildings.

  city
      A factor with levels: `city`, major city; `state`, state or
      state-remainder.

  conventional
      Percentage of households counted by conventional personal
      enumeration.

  undercount
      Preliminary estimate of percentage undercount.

  Ericksen, E. P., Kadane, J. B. and Tukey, J. W. (1989) Adjusting the
  1980 Census of Population and Housing. *Journal of the American
  Statistical Association* **84**, 927–944 [Tables 7 and 8].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ericksen.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 66 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ericksen.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Ericksen.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ericksen.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
