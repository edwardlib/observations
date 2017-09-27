# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def horse_kicks(path):
  """Death by Horse Kicks

  Data from von Bortkiewicz (1898), given by Andrews \\& Herzberg (1985),
  on number of deaths by horse or mule kicks in 10 (of 14 reported) corps
  of the Prussian army. 4 corps were not considered by Fisher (1925) as
  they had a different organization. This data set is a popular subset of
  the `VonBort` data.

  A 1-way table giving the number of deaths in 200 corps-years. The
  variable and its levels are

  No

  Name

  Levels

  1

  nDeaths

  0, 1, ..., 4

  Michael Friendly (2000), Visualizing Categorical Data, page 18.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `horse_kicks.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'horse_kicks.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/HorseKicks.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='horse_kicks.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
