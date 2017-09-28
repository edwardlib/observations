# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pines(path):
  """Pines

  Data from pine seedlings planted in 1990

  A dataset with 1000 observations on the following 15 variables.

  `Row`

  Row number in pine plantation

  `Col`

  Column number in pine plantation

  `Hgt90`

  Tree height at time of planting (cm)

  `Hgt96`

  Tree height in September 1996 (cm)

  `Diam96`

  Tree trunk diameter in September 1996 (cm)

  `Grow96`

  Leader growth during 1996 (cm)

  `Hgt97`

  Tree height in September 1997 (cm)

  `Diam97`

  Tree trunk diameter in September 1997 (cm)

  `Spread97`

  Widest lateral spread in September 1997 (cm)

  `Needles97`

  Needle length in September 1997 (mm)

  `Deer95`

  Type of deer damage in September 1995: 0 = none, 1 = browsed

  `Deer97`

  Type of deer damage in September 1997: 0 = none, 1 = browsed

  `Cover95`

  Thorny cover in September 1995: 0 = none; 1 = some; 2 = moderate; 3 =
  lots

  `Fert`

  Indicator for fertilizer: 0 = no, 1 = yes

  `Spacing`

  Distance (in feet) between trees (10 or 15)

  Thanks to the Kenyon College Department of Biology for sharing these

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pines.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1000 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pines.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Pines.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pines.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
