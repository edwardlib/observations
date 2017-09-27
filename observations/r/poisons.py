# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def poisons(path):
  """Animal Survival Times

  The `poisons` data frame has 48 rows and 3 columns.

  The data form a 3x4 factorial experiment, the factors being three
  poisons and four treatments. Each combination of the two factors was
  used for four animals, the allocation to animals having been completely
  randomized.

  This data frame contains the following columns:

  `time`
      The survival time of the animal in units of 10 hours.

  `poison`
      A factor with levels `1`, `2` and `3` giving the type of
      poison used.

  `treat`
      A factor with levels `A`, `B`, `C` and `D` giving the
      treatment.

  The data were obtained from

  Box, G.E.P. and Cox, D.R. (1964) An analysis of transformations (with
  Discussion). *Journal of the Royal Statistical Society, B*, **26**,
  211–252.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `poisons.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 48 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'poisons.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/poisons.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='poisons.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
