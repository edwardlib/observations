# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def islay(path):
  """Jura Quartzite Azimuths on Islay

  The `islay` data frame has 18 rows and 1 columns.

  Measurements were taken of paleocurrent azimuths from the Jura Quartzite
  on the Scottish island of Islay.

  This data frame contains the following column:

  `theta`
      The angle of the azimuth in degrees East of North.

  The data were obtained from

  Hand, D.J., Daly, F., Lunn, A.D., McConway, K.J. and Ostrowski, E.
  (1994) *A Handbook of Small Data Sets*, Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `islay.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'islay.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/islay.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='islay.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
