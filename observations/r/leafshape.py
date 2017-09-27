# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leafshape(path):
  """Full Leaf Shape Data Set

  Leaf length, width and petiole measurements taken at various sites in
  Australia.

  This data frame contains the following columns:

  bladelen
      leaf length (in mm)

  petiole
      a numeric vector

  bladewid
      leaf width (in mm)

  latitude
      latitude

  logwid
      natural logarithm of width

  logpet
      logarithm of petiole

  loglen
      logarithm of length

  arch
      leaf architecture (0 = plagiotropic, 1 = orthotropic

  location
      a factor with levels `Sabah`, `Panama`, `Costa Rica`,
      `N Queensland`, `S Queensland`, `Tasmania`

  King, D.A. and Maindonald, J.H. 1999. Tree architecture in relation to
  leaf dimensions and tree stature in temperate and tropical rain forests.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leafshape.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 286 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leafshape.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/leafshape.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leafshape.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
