# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def car(path):
  """Stated Preferences for Car Choice

  a cross-section

  *number of observations* : 4654

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  choice
      choice of a vehicle among 6 propositions

  college
      college education ?

  hsg2
      size of household greater than 2 ?

  coml5
      commute lower than 5 miles a day ?

  typez
      body type, one of regcar (regular car), sportuv (sport utility
      vehicle), sportcar, stwagon (station wagon), truck, van, for each
      proposition z from 1 to 6

  fuelz
      fuel for proposition z, one of gasoline, methanol, cng (compressed
      natural gas), electric.

  pricez
      price of vehicle divided by the logarithm of income

  rangez
      hundreds of miles vehicle can travel between refuelings/rechargings

  accz
      acceleration, tens of seconds required to reach 30 mph from stop

  speedz
      highest attainable speed in hundreds of mph

  pollutionz
      tailpipe emissions as fraction of those for new gas vehicle

  sizez
      0 for a mini, 1 for a subcompact, 2 for a compact and 3 for a
      mid–size or large vehicle

  spacez
      fraction of luggage space in comparable new gas vehicle

  costz
      cost per mile of travel (tens of cents) : home recharging for
      electric vehicle, station refueling otherwise

  stationz
      fraction of stations that can refuel/recharge vehicle

  McFadden, Daniel and Kenneth Train (2000) “Mixed MNL models for discrete
  response”, *Journal of Applied Econometrics*, **15(5)**, 447–470.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `car.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 4654 rows and 70 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'car.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Car.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='car.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
