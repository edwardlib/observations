# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def uk_driver_deaths(path):
  """Road Casualties in Great Britain 1969–84

  `UKDriverDeaths` is a time series giving the monthly totals of car
  drivers in Great Britain killed or seriously injured Jan 1969 to Dec
  1984. Compulsory wearing of seat belts was introduced on 31 Jan 1983.

  `Seatbelts` is more information on the same problem.

  `Seatbelts` is a multiple time series, with columns

  `DriversKilled`
      car drivers killed.

  `drivers`
      same as `UKDriverDeaths`.

  `front`
      front-seat passengers killed or seriously injured.

  `rear`
      rear-seat passengers killed or seriously injured.

  `kms`
      distance driven.

  `PetrolPrice`
      petrol price.

  `VanKilled`
      number of van (‘light goods vehicle’) drivers.

  `law`
      0/1: was the law in effect that month?

  Harvey, A.C. (1989) *Forecasting, Structural Time Series Models and the
  Kalman Filter.* Cambridge University Press, pp. 519–523.

  Durbin, J. and Koopman, S. J. (2001) *Time Series Analysis by State
  Space Methods.* Oxford University Press. http://www.ssfpack.com/dkbook/

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `uk_driver_deaths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 192 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'uk_driver_deaths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/UKDriverDeaths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='uk_driver_deaths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
