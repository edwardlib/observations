# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def wood(path):
  """Modified Data on Wood Specific Gravity

  The original data are from Draper and Smith (1966) and were used to
  determine the influence of anatomical factors on wood specific gravity,
  with five explanatory variables and an intercept. These data were
  contaminated by replacing a few observations with outliers.

  A data frame with 20 observations on the following 6 variables.

  x1, x2, x3, x4, x5
      explanatory “anatomical” wood variables.

  y
      wood specific gravity, the target variable.

  Draper and Smith (1966, p.227)

  Peter J. Rousseeuw and Annick M. Leroy (1987) *Robust Regression and
  Outlier Detection* Wiley, p.243, table 8.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `wood.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'wood.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/wood.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='wood.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
