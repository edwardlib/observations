# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def npr1(path):
  """US Naval Petroleum Reserve No. 1 data

  Data on the locations, porosity and permeability (a measure of oil flow)
  on 104 oil wells in the US Naval Petroleum Reserve No. 1 in California.

  This data frame contains the following columns:

  `x`
      x coordinates, in miles (origin unspecified)..

  `y`
      y coordinates, in miles.

  `perm`
      permeability in milli-Darcies.

  `por`
      porosity (%).

  Maher, J.C., Carter, R.D. and Lantz, R.J. (1975) Petroleum geology of
  Naval Petroleum Reserve No. 1, Elk Hills, Kern County, California. *USGS
  Professional Paper* **912**.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `npr1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 104 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'npr1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/npr1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='npr1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
