# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hitters(path):
  """Hitters Data

  This data set is deduced from the `Baseball` fielding data set:
  fielding performance basically includes the numbers of Errors, Putouts
  and Assists made by each player. In order to reduce the number of
  observations, the was compressed by calculating the mean number of
  errors, putouts and assists for each team and for only 6 positions (1B,
  2B, 3B, C, OF, SS and UT). In addition, each of these three variables
  was scaled to a common range by dividing each variable by the maximum of
  the variable.

  A data frame with 154 observations and 4 variables.

  Positions
      factor indicating the field position (1B=first baseman, 2B=second
      baseman, 3B=third baseman, C=catcher, OF=outfielder, SS=Short Stop,
      UT=Utility Players).

  Putouts
      occur when a fielder causes an opposing player to be tagged or
      forced out.

  Assists
      are credited to other fielders involved in making that putout.

  Errors
      count the errors made by a player.

  SAS System for Statistical Graphics, First Edition, Page A2.3

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hitters.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 322 rows and 20 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hitters.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Hitters.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hitters.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
