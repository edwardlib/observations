# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bomsoi(path):
  """Southern Oscillation Index Data

  The Southern Oscillation Index (SOI) is the difference in barometric
  pressure at sea level between Tahiti and Darwin. Annual SOI and
  Australian rainfall data, for the years 1900-2001, are given.
  Australia's annual mean rainfall is an area-weighted average of the
  total annual precipitation at approximately 370 rainfall stations around
  the country.

  This data frame contains the following columns:

  Year
      a numeric vector

  Jan
      average January SOI values for each year

  Feb
      average February SOI values for each year

  Mar
      average March SOI values for each year

  Apr
      average April SOI values for each year

  May
      average May SOI values for each year

  Jun
      average June SOI values for each year

  Jul
      average July SOI values for each year

  Aug
      average August SOI values for each year

  Sep
      average September SOI values for each year

  Oct
      average October SOI values for each year

  Nov
      average November SOI values for each year

  Dec
      average December SOI values for each year

  SOI
      a numeric vector consisting of average annual SOI values

  avrain
      a numeric vector consisting of a weighted average annual rainfall at
      a large number of Australian sites

  NTrain
      Northern Territory rain

  northRain
      north rain

  seRain
      southeast rain

  eastRain
      east rain

  southRain
      south rain

  swRain
      southwest rain

  Australian Bureau of Meteorology web pages:

  http://www.bom.gov.au/climate/change/rain02.txt and
  http://www.bom.gov.au/climate/current/soihtm1.shtml

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bomsoi.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 106 rows and 21 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bomsoi.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/bomsoi.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bomsoi.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
