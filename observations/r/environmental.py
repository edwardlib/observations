# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def environmental(path):
  """Atmospheric environmental conditions in New York City

  Daily measurements of ozone concentration, wind speed, temperature and
  solar radiation in New York City from May to September of 1973.

  A data frame with 111 observations on the following 4 variables.

  ozone
      Average ozone concentration (of hourly measurements) of in parts per
      billion.

  radiation
      Solar radiation (from 08:00 to 12:00) in langleys.

  temperature
      Maximum daily emperature in degrees Fahrenheit.

  wind
      Average wind speed (at 07:00 and 10:00) in miles per hour.

  Author(s)
  ~~~~~~~~~

  Documentation contributed by Kevin Wright.

  Bruntz, S. M., W. S. Cleveland, B. Kleiner, and J. L. Warner. (1974).
  The Dependence of Ambient Ozone on Solar Radiation, Wind, Temperature,
  and Mixing Height. In *Symposium on Atmospheric Diffusion and Air
  Pollution*, pages 125–128. American Meterological Society, Boston.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `environmental.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 111 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'environmental.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/lattice/environmental.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='environmental.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
