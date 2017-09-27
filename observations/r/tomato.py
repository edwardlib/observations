# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tomato(path):
  """Root weights of tomato plants exposed to 4 different treatments

  The `tomato` data frame has 24 rows and 2 columns. They are from an
  experiment that exposed tomato plants to four different 'nutrients'.

  This data frame contains the following columns:

  weight
      weight, in g

  trt
      a factor with levels `water only`, `conc nutrient`,
      `2-4-D + conc nutrient`, `3x conc nutrient`

  Dr Ron Balham, Victoria University of Wellington NZ, sometime in 1971 -
  1976.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tomato.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tomato.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/tomato.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tomato.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
