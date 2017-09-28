# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cooling_water(path):
  """CoolingWater

  Temperature of a mug of water as it cools

  A data frame with 222 observations of the following variables.

  -  `time` time in minutes

  -  `temp` temperature in Celsius

  These data were collected Stan Wagon to help his mathematical modeling
  students explore Newton's Law of Cooling and the ways that the law is
  really only an approximation. More about Stan: http://stanwagon.com.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cooling_water.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 222 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cooling_water.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/CoolingWater.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cooling_water.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
