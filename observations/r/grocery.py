# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grocery(path):
  """Grocery

  Grocery store sales

  A dataset with 36 observations on the following 5 variables.

  `Discount`

  Amount of discount: `5.00%`, `10.00%` or `15.00%`

  `Store`

  Store number (1-12)

  `Display`

  `Featured End of Aisl`, `Featured Middle of A`, or `Not Featured`

  `Sales`

  Number sold during one week

  `Price`

  Wholesale price (in dollars)

  These data are not real, though they are simulated to approximate an
  actual study. The data come from John Grego, Director of the Stat Lab at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grocery.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grocery.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Grocery.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grocery.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
