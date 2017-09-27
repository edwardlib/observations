# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def agefat(path):
  """Total Body Composision Data

  Age and body fat percentage of 25 normal adults.

  A data frame with 25 observations on the following 3 variables.

  `age`
      the age of the subject.

  `fat`
      the body fat percentage.

  `sex`
      a factor with levels `female` and `male`.

  R. B. Mazess, W. W. Peppler and M. Gibbons (1984), Total body
  composition by dual-photon (153Gd) absorptiometry. *American Journal of
  Clinical Nutrition*, **40**, 834–839.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `agefat.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 25 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'agefat.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/agefat.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='agefat.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
