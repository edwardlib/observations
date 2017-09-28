# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def road(path):
  """Road Accident Deaths in US States

  A data frame with the annual deaths in road accidents for half the US
  states.

  Columns are:

  `state`
      name.

  `deaths`
      number of deaths.

  `drivers`
      number of drivers (in 10,000s).

  `popden`
      population density in people per square mile.

  `rural`
      length of rural roads, in 1000s of miles.

  `temp`
      average daily maximum temperature in January.

  `fuel`
      fuel consumption in 10,000,000 US gallons per year.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `road.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'road.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/road.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='road.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
