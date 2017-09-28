# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def progression(path):
  """Progression of Record times for track races, 1912 - 2008

  Progression in world record times for track and road races.

  A data frame with 227 observations on the following 4 columns.

  `year`
      Year that time was first recorded

  `Distance`
      distance in kilometers

  `Time`
      time in minutes

  `race`
      character; descriptor for event (100m, mile, ...)

  Links to sources for the data are at

  http://en.wikipedia.org/wiki/Athletics_world_record

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `progression.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 227 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'progression.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/progression.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='progression.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
