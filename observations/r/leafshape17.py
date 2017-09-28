# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leafshape17(path):
  """Subset of Leaf Shape Data Set

  The `leafshape17` data frame has 61 rows and 8 columns. These are leaf
  length, width and petiole measurements taken at several sites in
  Australia. This is a subset of the `leafshape` data frame.

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
      logarithm of petiole measurement

  loglen
      logarithm of length

  arch
      leaf architecture (0 = orthotropic, 1 = plagiotropic)

  King, D.A. and Maindonald, J.H. 1999. Tree architecture in relation to
  leaf dimensions and tree stature in temperate and tropical rain forests.
  Journal of Ecology 87: 1012-1024.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leafshape17.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 61 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leafshape17.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/leafshape17.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leafshape17.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
