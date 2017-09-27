# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def world_records(path):
  """Record times for track and road races, at August 9th 2006

  Record times for track and road races, at August 9th 2006

  A data frame with 40 observations on the following 9 variables.

  `Distance`
      distance in kilometers

  `roadORtrack`
      a factor with levels `road` `track`

  `Place`
      place; a character vector

  `Time`
      time in minutes

  `Date`
      a Date

  http://www.gbrathletics.com/wrec.htm

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `world_records.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'world_records.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/worldRecords.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='world_records.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
