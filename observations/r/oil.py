# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def oil(path):
  """Oil Investment

  a cross-section from 1969 to 1992

  *number of observations* : 53

  *observation* : production units

  *country* : United Kingdown

  A dataframe containing :

  dur
      duration of the appraisal lag in months (time span between discovery
      of an oil field and beginning of development, i.e. approval of annex
      B).

  size
      size of recoverable reserves in millions of barrels

  waterd
      depth of the sea in metres

  gasres
      size of recoverable gas reserves in billions of cubic feet

  operator
      equity market value (in 1991 million pounds) of the company
      operating the oil field

  p
      real after–tax oil price measured at time of annex B approval

  vardp
      volatility of the real oil price process measured as the squared
      recursive standard errors of the regression of pt-pt-1 on a constant

  p97
      adaptive expectations (with parameter theta=0.97) for the real
      after–tax oil prices formed at the time of annex B approval

  varp97
      volatility of the adaptive expectations (with parameter theta=0.97)
      for real after tax oil prices measured as the squared recursive
      standard errors of the regression of pt on pte(theta)

  p98
      adaptive expectations (with parameter theta=0.98) for the real
      after–tax oil prices formed at the time of annex B approval

  varp98
      volatility of the adaptive expectations (with parameter theta=0.98)
      for real after tax oil prices measured as the squared recursive
      standard errors of the regression of pt on pte(theta)

  Favero, Carlo A., M. Hashem Pesaran and Sunil Sharma (1994) “A duration
  model of irreversible oil investment : theory and empirical evidence”,
  *Journal of Applied Econometrics*, **9(S)**, S95–S112.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `oil.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 53 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'oil.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Oil.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='oil.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
