# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ships(path):
  """Ships Damage Data

  Data frame giving the number of damage incidents and aggregate months of
  service by ship type, year of construction, and period of operation.

  `type`
      type: `"A"` to `"E"`.

  `year`
      year of construction: 1960–64, 65–69, 70–74, 75–79 (coded as
      `"60"`, `"65"`, `"70"`, `"75"`).

  `period`
      period of operation : 1960–74, 75–79.

  `service`
      aggregate months of service.

  `incidents`
      number of damage incidents.

  P. McCullagh and J. A. Nelder, (1983), *Generalized Linear Models.*

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ships.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 40 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ships.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/ships.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ships.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
