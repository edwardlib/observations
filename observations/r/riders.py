# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def riders(path):
  """Volume of Users of a Massachusetts Rail Trail

  The Pioneer Valley Planning Commission (PVPC) collected data north of
  Chestnut Street in Florence, MA for ninety days from April 5, 2005 to
  November 15, 2005. Data collectors set up a laser sensor, with breaks in
  the laser beam recording when a rail-trail user passed the data
  collection station.

  A data frame with 90 observations on the following 12 variables.

  `date`
      date of data collection (POSIXct)

  `day`
      a factor with levels `Monday`, `Tuesday`, `Wednesday`,
      `Thursday`, `Friday`, `Saturday`, and `Sunday`.

  `highT`
      high temperature for the day (in degrees Fahrenheit)

  `lowT`
      low temperature for the day (in degrees Fahrenheit)

  `hi`
      shorter name for `highT`

  `lo`
      shorter name for `lowT`

  `precip`
      inches of precipitation

  `clouds`
      measure of cloud cover (in oktas)

  `riders`
      estimated number of trail crossings that day (number of breaks
      recorded)

  `ct`
      shorter name for `riders`

  `weekday`
      type of day: a factor with levels `N` (weekend or holiday) `Y`
      (non-holiday weekday)

  `wday`
      shorter name for `weekday`

  Pioneer Valley Planning Commission,
  http://www.fvgreenway.org/pdfs/Northampton-Bikepath-Volume-Counts

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `riders.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'riders.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Riders.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='riders.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
