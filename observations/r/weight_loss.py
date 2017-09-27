# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def weight_loss(path):
  """Weight Loss Data

  Contrived data on weight loss and self esteem over three months, for
  three groups of individuals: Control, Diet and Diet + Exercise. The data
  constitute a double-multivariate design.

  A data frame with 34 observations on the following 7 variables.

  `group`
      a factor with levels `Control` `Diet` `DietEx`.

  `wl1`
      Weight loss at 1 month

  `wl2`
      Weight loss at 2 months

  `wl3`
      Weight loss at 3 months

  `se1`
      Self esteem at 1 month

  `se2`
      Self esteem at 2 months

  `se3`
      Self esteem at 3 months

  Originally taken from http://www.csun.edu/~ata20315/psy524/main.htm, but

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `weight_loss.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 34 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'weight_loss.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/WeightLoss.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='weight_loss.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
