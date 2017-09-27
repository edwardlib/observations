# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ethanol1(path):
  """Ethanol

  Ethanol

  A dataset with 16 observations on the following 3 variables.

  `Sugar`

  Type of sugar: `Galactose` or `Glucose`

  `O2Conc`

  Oxygen concentration

  `Ethanol`

  Ethanol concentration

  Data are found in Statistics: The Exploration and Analysis of Data by
  Jay Devore and Roxy Peck (1960). St. Paul, MN: West.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ethanol1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ethanol1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Ethanol.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ethanol1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
