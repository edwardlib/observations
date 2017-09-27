# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def davis(path):
  """Self-Reports of Height and Weight

  The `Davis` data frame has 200 rows and 5 columns. The subjects were
  men and women engaged in regular exercise. There are some missing data.

  This data frame contains the following columns:

  sex
      A factor with levels: `F`, female; `M`, male.

  weight
      Measured weight in kg.

  height
      Measured height in cm.

  repwt
      Reported weight in kg.

  repht
      Reported height in cm.

  Personal communication from C. Davis, Departments of Physical Education
  and Psychology, York University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `davis.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 200 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'davis.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Davis.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='davis.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
