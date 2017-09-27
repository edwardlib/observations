# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def modelcars(path):
  """Model Car Data

  The `modelcars` data frame has 12 rows and 2 columns. The data are for
  an experiment in which a model car was released three times at each of
  four different distances up a 20 degree ramp. The experimenter recorded
  distances traveled from the bottom of the ramp across a concrete floor.

  This data frame contains the following columns:

  distance.traveled
      a numeric vector consisting of the lengths traveled (in cm)

  starting.point
      a numeric vector consisting of the distance of the starting point
      from the top of the ramp (in cm)

  W.J. Braun

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `modelcars.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'modelcars.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/modelcars.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='modelcars.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
