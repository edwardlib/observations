# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def kids198(path):
  """Kids198

  Measurements of Children

  A dataset with 198 observations on the following 5 variables.

  `Height`

  Height (in inches)

  `Weight`

  Weight (in pounds)

  `Age`

  Age (in months)

  `Sex`

  `0`\ =male or `1`\ =female

  `Race`

  `0`\ =white or `1`\ =other

  A sample of 198 cases from the NIST's AnthroKids dataset at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `kids198.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 198 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'kids198.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/Kids198.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='kids198.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
