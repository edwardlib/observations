# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def natural_park(path):
  """Willingness to Pay for the Preservation of the Alentejo Natural Park

  a cross-section from 1987

  *number of observations* : 312

  *observation* : individuals

  *country* : Portugal

  A dataframe containing :

  bid1
      initial bid, in euro

  bidh
      higher bid

  bidl
      lower bid

  answers
      a factor with levels (nn,ny,yn,yy)

  age
      age in 6 classes

  sex
      a factor with levels (male,female)

  income
      income in 8 classes

  Nunes, Paulo (2000) *Contingent Valuation of the Benefits of natural
  areas and its warmglow component*, PhD thesis 133, FETEW, KULeuven.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `natural_park.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 312 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'natural_park.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/NaturalPark.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='natural_park.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
