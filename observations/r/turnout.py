# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def turnout(path):
  """Turnout Data Set from the National Election Survey

  This data set contains individual-level turnout data. It pools several
  American National Election Surveys conducted during the 1992
  presidential election year. Only the first 2,000 observations (from a
  total of 15,837 observations) are included in the sample data.

  A table containing 5 variables ("race", "age", "educate", "income", and
  "vote") and 2,000 observations.

  National Election Survey

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `turnout.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2000 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'turnout.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/turnout.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='turnout.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
