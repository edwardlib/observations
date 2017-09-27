# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def infant_mortality(path):
  """InfantMortality

  Infant mortality rates in the United States (1920-2000)

  A dataset with 9 observations on the following 2 variables.

  `Mortality`

  Deaths witin one year of birth (per 1000 births

  `Year`

  1920-2000 (by decades)

  CDC National Vital Statistics Reports at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `infant_mortality.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'infant_mortality.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/InfantMortality.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='infant_mortality.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
