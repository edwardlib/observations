# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def orings(path):
  """Challenger O-rings Data

  Record of the number and type of O-ring failures prior to the tragic
  Challenger mission in January, 1986.

  This data frame contains the following columns:

  Temperature
      O-ring temperature for each test firing or actual launch of the
      shuttle rocket engine

  Erosion
      Number of erosion incidents

  Blowby
      Number of blowby incidents

  Total
      Total number of incidents

  Presidential Commission on the Space Shuttle Challenger Accident, Vol.
  1, 1986: 129-131.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `orings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'orings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/orings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='orings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
