# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def antigua(path):
  """Averages by block of yields for the Antigua Corn data

  These data frames have yield averages by blocks (parcels). The
  `ant111b` data set is a subset of this.

  A data frame with 324 observations on 7 variables.

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

  ears
      a numeric vector; note that -9999 is used as a missing value code.

  harvwt
      a numeric vector; the average yield

  Andrews DF; Herzberg AM, 1985. Data. A Collection of Problems from Many
  Fields for the Student and Research Worker. Springer-Verlag. (pp.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `antigua.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 288 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'antigua.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/antigua.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='antigua.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
