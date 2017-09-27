# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def humanpower2(path):
  """Oxygen uptake versus mechanical power, for humans

  The data set from Daedalus project.

  A data frame with 28 observations on the following 3 variables.

  wattsPerKg
      a numeric vector: watts per kilogram of body weight

  o2
      a numeric vector: ml/min/kg

  id
      a factor with levels 1 - 5 (`humanpower1`) or 1 - 4
      (`humanpower2`), identifying the different athletes

  Bussolari, S.R.(1987). Human factors of long-distance human-powered
  aircraft flights. Human Power 5: 8-12.

  Nadel and Bussolari, S.R.(1988). The Daedalus project: physiological
  problems and solutions. American Scientist 76: 351-360.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `humanpower2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 26 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'humanpower2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/humanpower2.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='humanpower2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
