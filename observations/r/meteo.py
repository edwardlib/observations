# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def meteo(path):
  """Meteorological Measurements for 11 Years

  Several meteorological measurements for a period between 1920 and 1931.

  A data frame with 11 observations on the following 6 variables.

  `year`
      the years.

  `rainNovDec`
      rainfall in November and December (mm).

  `temp`
      average July temperature.

  `rainJuly`
      rainfall in July (mm).

  `radiation`
      radiation in July (millilitres of alcohol).

  `yield`
      average harvest yield (quintals per hectare).

  B. S. Everitt and G. Dunn (2001), *Applied Multivariate Data Analysis*,
  2nd edition, Arnold, London.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `meteo.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'meteo.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/meteo.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='meteo.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
