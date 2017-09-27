# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def n_ox_emissions(path):
  """NOx Air Pollution Data

  A typical medium sized environmental data set with hourly measurements
  of *NOx* pollution content in the ambient air.

  A data frame with 8088 observations on the following 4 variables.

  `julday`
      day number, a factor with levels `373` ... `730`, typically with
      24 hourly measurements.

  `LNOx`
      *\\log* of hourly mean of NOx concentration in ambient air [ppb]
      next to a highly frequented motorway.

  `LNOxEm`
      *\\log* of hourly sum of NOx emission of cars on this motorway in
      arbitrary units.

  `sqrtWS`
      Square root of wind speed [m/s].

  René Locher (at ZHAW, Switzerland).

  See Also
  ~~~~~~~~

  another NOx dataset, `ambientNOxCH`.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `n_ox_emissions.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8088 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'n_ox_emissions.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/NOxEmissions.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='n_ox_emissions.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
