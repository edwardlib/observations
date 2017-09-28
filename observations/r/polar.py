# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def polar(path):
  """Pole Positions of New Caledonian Laterites

  The `polar` data frame has 50 rows and 2 columns.

  The data are the pole positions from a paleomagnetic study of New
  Caledonian laterites.

  This data frame contains the following columns:

  `lat`
      The latitude (in degrees) of the pole position. Note that all
      latitudes are negative as the axis is taken to be in the lower
      hemisphere.

  `long`
      The longitude (in degrees) of the pole position.

  The data were obtained from

  Fisher, N.I., Lewis, T. and Embleton, B.J.J. (1987) *Statistical
  Analysis of Spherical Data*. Cambridge University Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `polar.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'polar.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/polar.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='polar.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
