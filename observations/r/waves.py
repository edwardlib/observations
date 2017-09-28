# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def waves(path):
  """Electricity from Wave Power at Sea

  Measurements of root mean square bending moment by two different mooring
  methods.

  A data frame with 18 observations on the following 2 variables.

  method1
      Root mean square bending moment in Newton metres, mooring method 1

  method2
      Root mean square bending moment in Newton metres, mooring method 2

  D. J. Hand, F. Daly, A. D. Lunn, K. J. McConway and E. Ostrowski (1994).
  *A Handbook of Small Datasets*, Chapman and Hall/CRC, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `waves.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'waves.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/waves.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='waves.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
