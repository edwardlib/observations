# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def airmay(path):
  """Air Quality Data

  Air Quality Data Set for May 1973, from Chambers et al. (1983). The
  whole data set consists of daily readings of air quality values from May
  1, 1973 to September 30, 1973, but here are included only the values for
  May. This data set is an example of the special treatment of the missing
  values.

  A data frame with 31 observations on the following 4 variables.

  `X1`
      Solar Radiation in Longleys in the frequency band 4000-7700 from
      0800 to 1200 hours at Central Park

  `X2`
      Average windspeed (in miles per hour) between 7000 and 1000 hours at
      La Guardia Airport

  `X3`
      Maximum daily temperature (in degrees Fahrenheit) at La Guardia
      Airport

  `Y`
      Mean ozone concentration (in parts per billion) from 1300 to 1500
      hours at Roosevelt Island

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.86, table 6.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `airmay.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 31 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'airmay.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/airmay.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='airmay.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
