# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def frogs(path):
  """Frogs Data

  The `frogs` data frame has 212 rows and 11 columns. The data are on
  the distribution of the Southern Corroboree frog, which occurs in the
  Snowy Mountains area of New South Wales, Australia.

  This data frame contains the following columns:

  pres.abs
      0 = frogs were absent, 1 = frogs were present

  northing
      reference point

  easting
      reference point

  altitude
      altitude , in meters

  distance
      distance in meters to nearest extant population

  NoOfPools
      number of potential breeding pools

  NoOfSites
      (number of potential breeding sites within a 2 km radius

  avrain
      mean rainfall for Spring period

  meanmin
      mean minimum Spring temperature

  meanmax
      mean maximum Spring temperature

  Hunter, D. (2000) The conservation and demography of the southern
  corroboree frog (Pseudophryne corroboree). M.Sc. thesis, University of
  Canberra, Canberra.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `frogs.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 212 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'frogs.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/frogs.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='frogs.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
