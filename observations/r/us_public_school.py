# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def us_public_school(path):
  """U. S. State Public-School Expenditures

  The `Anscombe` data frame has 51 rows and 4 columns. The observations
  are the U. S. states plus Washington, D. C. in 1970.

  This data frame contains the following columns:

  education
      Per-capita education expenditures, dollars.

  income
      Per-capita income, dollars.

  young
      Proportion under 18, per 1000.

  urban
      Proportion urban, per 1000.

  Anscombe, F. J. (1981) *Computing in Statistical Science Through APL*.
  Springer-Verlag.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `us_public_school.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 51 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'us_public_school.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Anscombe.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='us_public_school.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
