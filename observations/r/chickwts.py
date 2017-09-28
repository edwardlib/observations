# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chickwts(path):
  """Chicken Weights by Feed Type

  An experiment was conducted to measure and compare the effectiveness of
  various feed supplements on the growth rate of chickens.

  A data frame with 71 observations on the following 2 variables.

  `weight`
      a numeric variable giving the chick weight.

  `feed`
      a factor giving the feed type.

  Anonymous (1948) *Biometrika*, **35**, 214.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chickwts.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 71 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chickwts.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/chickwts.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chickwts.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
