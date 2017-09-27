# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chest_sizes(path):
  """Chest measurements of 5738 Scottish Militiamen

  Quetelet's data on chest measurements of 5738 Scottish Militiamen.
  Quetelet (1846) used this data as a demonstration of the normal
  distribution of physical characteristics.

  A data frame with 16 observations on the following 2 variables.

  `chest`
      Chest size (in inches)

  `count`
      Number of soldiers with this chest size

  Velleman, P. F. and Hoaglin, D. C. (1981). *Applications, Basics, and
  Computing of Exploratory Data Analysis*. Belmont. CA: Wadsworth.
  Retrieved from Statlib:
  `https://www.stat.cmu.edu/StatDat/Datafiles/MilitiamenChests.html`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chest_sizes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 16 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chest_sizes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/ChestSizes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chest_sizes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
