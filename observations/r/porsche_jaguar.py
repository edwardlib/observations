# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def porsche_jaguar(path):
  """PorscheJaguar

  Compare prices for Porsche and Jaguar cars offered for sale at an
  internet site

  A dataset with 60 observations on the following 5 variables.

  `Car`

  Car model: `Jaguar` or `Porsche`

  `Price`

  Price (in $1,000's)

  `Age`

  Age of the car (in years)

  `Mileage`

  Previous miles driven (in 1,000's)

  `Porsche`

  Indicator for Porsche (`1`) or Jaguar (`0`)


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `porsche_jaguar.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'porsche_jaguar.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/PorscheJaguar.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='porsche_jaguar.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
