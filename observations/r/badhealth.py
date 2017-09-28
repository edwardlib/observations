# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def badhealth(path):
  """badhealth

  From German health survey data for the year 1998 only.

  A data frame with 1,127 observations on the following 3 variables.

  `numvisit`
      number of visits to doctor during 1998

  `badh`
      1=patient claims to be in bad health; 0=not in bad health

  `age`
      age of patient: 20-60

  German Health Survey, amended in Hilbe and Greene (2008).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `badhealth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1127 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'badhealth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/COUNT/badhealth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='badhealth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
