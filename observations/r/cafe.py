# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cafe(path):
  """CAFE

  Senate votes for Corporate Average Fuel Economy (CAFE) bill

  A dataset with 100 observations on the following 7 variables.

  `Senator`

  Senator's name

  `State`

  Code for senator's state

  `Party`

  party affiliation: `D`\ =Democrat, `I`\ =Independent,
  `R`\ =Republican

  `Contribution`

  Contributions from car manufactures (dollars)

  `LogContr`

  Log of (Contribution+1)

  `Dem`

  `1`\ =Democrat/Indpendent `0`\ =Republican

  `Vote`

  `1`\ =yes or `0`\ =no


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cafe.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cafe.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/CAFE.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cafe.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
