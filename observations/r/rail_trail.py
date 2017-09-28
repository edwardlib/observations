# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rail_trail(path):
  """Volume of Users of a Rail Trail

  The Pioneer Valley Planning Commission (PVPC) collected data north of
  Chestnut Street in Florence, MA for ninety days from April 5, 2005 to
  November 15, 2005. Data collectors set up a laser sensor, with breaks in
  the laser beam recording when a rail-trail user passed the data
  collection station.

  A data frame with 90 observations on the following variables.

  -  `hightemp` daily high temperature (in degrees Fahrenheit)

  -  `lowtemp` daily low temperature (in degrees Fahrenheit)

  -  `avgtemp` average of daily low and daily high temperature (in
     degrees Fahrenheit)

  -  `spring` indicator of whether the season was Spring

  -  `summer` indicator of whether the season was Summer

  -  `fall` indicator of whether the season was Fall

  -  `cloudcover` measure of cloud cover (in oktas)

  -  `precip` measure of precipitation (in inches)

  -  `volume` estimated number of trail users that day (number of breaks
     recorded)

  -  `weekday` indicator of whether the day was a non-holiday weekday

  Pioneer Valley Planning Commission

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rail_trail.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 90 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rail_trail.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/RailTrail.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rail_trail.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
