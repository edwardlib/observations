# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sugar(path):
  """Sugar Data

  The `sugar` data frame has 12 rows and 2 columns. They are from an
  experiment that compared an unmodified wild type plant with three
  different genetically modified forms. The measurements are weights of
  sugar that were obtained by breaking down the cellulose.

  This data frame contains the following columns:

  weight
      weight, in mg

  trt
      a factor with levels `Control` i.e. unmodified Wild form, `A`
      Modified 1, `B` Modified 2, `C` Modified 3

  Anonymous

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sugar.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sugar.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/sugar.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sugar.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
