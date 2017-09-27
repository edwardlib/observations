# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def seedrates(path):
  """Barley Seeding Rate Data

  The `seedrates` data frame has 5 rows and 2 columns on the effect of
  seeding rate of barley on yield.

  This data frame contains the following columns:

  rate
      the seeding rate

  grain
      the number of grain per head of barley

  McLeod, C.C. 1982. Effect of rates of seeding on barley grown for grain.
  New Zealand Journal of Agriculture 10: 133-136.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `seedrates.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'seedrates.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/seedrates.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='seedrates.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
