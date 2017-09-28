# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def st_vincent(path):
  """Averages by block of yields for the St. Vincent Corn data

  These data frames have yield averages by blocks (parcels).

  A data frame with 324 observations on 8 variables.

  code
      a numeric vector

  island
      a numeric vector

  id
      a numeric vector

  site
      a factor with 8 levels.

  block
      a factor with levels `I` `II` `III` `IV`

  plot
      a numeric vector

  trt
      a factor consisting of 12 levels

  harvwt
      a numeric vector; the average yield

  Andrews DF; Herzberg AM, 1985. Data. A Collection of Problems from Many
  Fields for the Student and Research Worker. Springer-Verlag. (pp.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `st_vincent.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 324 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'st_vincent.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/stVincent.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='st_vincent.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
