# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def suicide(path):
  """Suicide Rates in Germany

  Data from Heuer (1979) on suicide rates in West Germany classified by
  age, sex, and method of suicide.

  A data frame with 306 observations and 6 variables.

  Freq
      frequency of suicides.

  sex
      factor indicating sex (male, female).

  method
      factor indicating method used.

  age
      age (rounded).

  age.group
      factor. Age classified into 5 groups.

  method2
      factor indicating method used (same as `method` but some levels
      are merged).

  Michael Friendly (2000), Visualizing Categorical Data:
  http://euclid.psych.yorku.ca/ftp/sas/vcd/catdata/suicide.sas

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `suicide.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 306 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'suicide.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Suicide.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='suicide.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
