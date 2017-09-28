# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def space_shuttle(path):
  """Space Shuttle O-ring Failures

  Data from Dalal et al. (1989) about O-ring failures in the NASA space
  shuttle program. The damage index comes from a discussion of the data by
  Tufte (1997).

  A data frame with 24 observations and 6 variables.

  FlightNumber
      Number of space shuttle flight.

  Temperature
      temperature during start (in degrees F).

  Pressure
      pressure.

  Fail
      did any O-ring failures occur? (no, yes).

  nFailures
      how many (of six) 0-rings failed?.

  Damage
      damage index.

  Michael Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/orings.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `space_shuttle.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'space_shuttle.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/SpaceShuttle.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='space_shuttle.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
