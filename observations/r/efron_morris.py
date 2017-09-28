# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def efron_morris(path):
  """Batting Averages for 18 major league baseball players, 1970

  Batting averages for 18 major league baseball players, first 45 at bats
  of the 1970 season.

  `name`
      character, name of player

  `team`
      character, team of player, abbreviated

  `league`
      character, National League or American League

  `r`
      numeric, hits in 1st 45 at bats

  `y`
      numeric, `r`/45, batting average over 1st 45 at bats

  `n`
      numeric, number of at bats, remainder of 1970 season

  `p`
      numeric, batting average over remainder of 1970 season

  Efron, Bradley and Carl Morris. 1975. Data Analysis Using Stein's
  Estimator and Its Generalizations. *Journal of the American Statistical
  Association*. 70:311-319.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `efron_morris.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 18 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'efron_morris.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/EfronMorris.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='efron_morris.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
