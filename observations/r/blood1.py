# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def blood1(path):
  """Blood1

  Systolic blood pressure for a sample of 500 adults

  A dataset with 500 observations on the following 3 variables.

  `SystolicBP`

  Systolic blood pressure (mm of Hg)

  `Smoke`

  `Y`\ =smoker or `N`\ =non-smoker

  `Overwt`

  `1`\ =normal, `2`\ =overweight, or `3`\ =obese

  | Data are part of a larger case study for the 2003 Annual Meeting of
    the Statistical Society of Canada.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `blood1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 500 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'blood1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Blood1.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='blood1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
