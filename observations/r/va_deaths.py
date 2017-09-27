# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def va_deaths(path):
  """Death Rates in Virginia (1940)

  Death rates per 1000 in Virginia in 1940.

  A matrix with 5 rows and 4 columns.

  Molyneaux, L., Gilliam, S. K., and Florant, L. C.(1947) Differences in
  Virginia death rates by color, sex, age, and rural or urban residence.
  *American Sociological Review*, **12**, 525–535.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `va_deaths.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'va_deaths.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/VADeaths.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='va_deaths.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
