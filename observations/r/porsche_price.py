# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def porsche_price(path):
  """PorschePrice

  Prices for Porsche cars offered for sale at an internet site.

  A dataset with 30 observations on the following 3 variables.

  `Price`

  Asking price for the car (in $1,000's)

  `Age`

  Age of the car (in years)

  `Mileage`

  Previous miles driven (in 1,000's)

  Data collected for a student project from autotrader.com in February

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `porsche_price.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'porsche_price.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/PorschePrice.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='porsche_price.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
