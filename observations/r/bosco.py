# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bosco(path):
  """Boscovich Data

  Boscovich data used to estimate the ellipticity of the earth. There are
  five measurements of the arc length of one degree of latitude taken at 5
  different latitudes. See Koenker (2005) for further details and
  references.

  A data frame containing 5 observations on 2 variables

  x
      sine squared of latitude measured in degrees

  y
      arc length of one degree of latitude measured in toise - 56,700, one
      toise approximately equals 1.95 meters.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bosco.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bosco.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/quantreg/Bosco.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bosco.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
