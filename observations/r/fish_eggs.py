# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def fish_eggs(path):
  """FishEggs

  Fish Eggs

  A dataset with 35 observations on the following 4 variables.

  `Age`

  Age of the fish (in years)

  `PctDM`

  Percentage of the total egg material that is solid

  `Month`

  Month fish was caught: `Sep`\ =September or `Nov`\ =November

  `Sept`

  Indicator with `1`\ =September or `0`\ =November

  Lantry, OGorman, and Machut (2008) "Maternal Characteristics versus Egg
  Size and Energy Density," Journal of Great Lakes Research 34(4):

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `fish_eggs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 35 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'fish_eggs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/FishEggs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='fish_eggs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
