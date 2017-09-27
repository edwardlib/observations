# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def freedman(path):
  """Crowding and Crime in U. S. Metropolitan Areas

  The `Freedman` data frame has 110 rows and 4 columns. The observations
  are U. S. metropolitan areas with 1968 populations of 250,000 or more.
  There are some missing data.

  This data frame contains the following columns:

  population
      Total 1968 population, 1000s.

  nonwhite
      Percent nonwhite population, 1960.

  density
      Population per square mile, 1968.

  crime
      Crime rate per 100,000, 1969.

  United States (1970) *Statistical Abstract of the United States*. Bureau
  of the Census.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `freedman.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 110 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'freedman.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Freedman.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='freedman.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
