# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cloud(path):
  """Cloud point of a Liquid

  This data set contains the measurements concerning the cloud point of a
  Liquid, from Draper and Smith (1969). The cloud point is a measure of
  the degree of crystallization in a stock.

  A data frame with 19 observations on the following 2 variables.

  `Percentage`
      Percentage of I-8

  `CloudPoint`
      Cloud point

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.96, table 10.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cloud.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 19 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cloud.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/cloud.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cloud.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
