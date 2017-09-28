# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grog(path):
  """Alcohol consumption in Australia and New Zealand

  Data are annual apparent alcohol consumption in Australia and New
  Zealand, in liters of pure alcohol content per annum, separately for
  beer, wine, and spirits (including spirit-based products).

  A data frame with 18 observations on the following 5 variables.

  `Beer`
      liters per annum

  `Wine`
      liters per annum

  `Spirit`
      liters per annum

  `Country`
      a factor with levels `Australia` `NewZealand`

  `Year`
      Year ending in June of the given year

  Australian data are from http://www.abs.gov.au. For New Zealand data, go
  to http://www.stats.govt.nz/infoshare/ Click on 'Industry sectors' and
  then on 'Alcohol Available for Consumption - ALC'.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grog.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grog.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/grog.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grog.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
