# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bird_nest(path):
  """BirdNest

  Data on bird nests

  A dataset with 84 observations on the following 12 variables.

  `Species`

  Latin species name

  `Common`

  Common species name

  `Page`

  Page in a bird manual describing the species

  `Length`

  Mean body length for the species (in cm)

  `Nesttype`

  Type of nest

  `Location`

  Location of nest

  `No.eggs`

  Number of eggs

  `Color`

  a numeric vector

  `Incubate`

  Mean length of time (in days) the species incubates eggs in the nest

  `Nestling`

  Mean length of time (in days) the species cares for babies in the nest
  until fledged

  `Totcare`

  Total care time = Incubate+Nestling

  `Closed`

  1=closed nest (pendant, spherical, cavity, crevice, burrow), 0=open nest
  (saucer, cup)

  Project by Amy Moore at Grinnell College

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bird_nest.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 84 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bird_nest.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/BirdNest.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bird_nest.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
