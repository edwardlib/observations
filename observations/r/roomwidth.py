# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def roomwidth(path):
  """Students Estimates of Lecture Room Width

  Lecture room width estimated by students in two different units.

  A data frame with 113 observations on the following 2 variables.

  unit
      a factor with levels `feet` and `metres`.

  width
      the estimated width of the lecture room.

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `roomwidth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 113 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'roomwidth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/roomwidth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='roomwidth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
