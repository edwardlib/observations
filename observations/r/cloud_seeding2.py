# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cloud_seeding2(path):
  """Cloud Seeding 2

  Rainfall amounts from a cloud seeding experiment

  A dataset with 108 observations on the following 8 variables.

  `Period`

  ID for time period

  `Seeded`

  Treatment coded as `S`\ =seded or `U`\ =unseeded

  `Season`

  Coded as `Autumn`, `Spring`, `Summer`, or `Winter`

  `TE`

  Rainfall in East (treatment)

  `TW`

  Rainfall in West (treatment

  `NC`

  Rainfall in North (control)

  `SC`

  Rainfall in South (control)

  `NWC`

  Rainfall in Northwest (control)

  Data were accessed from the website
  www.statsci.org/data/oz/cloudtas.html. This is the web home of the
  Australasian Data and Story Library (OzDASL).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cloud_seeding2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 108 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cloud_seeding2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/CloudSeeding2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cloud_seeding2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
