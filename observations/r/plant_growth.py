# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def plant_growth(path):
  """Results from an Experiment on Plant Growth

  Results from an experiment to compare yields (as measured by dried
  weight of plants) obtained under a control and two different treatment
  conditions.

  A data frame of 30 cases on 2 variables.

  +---------+----------+-----------+
  | [, 1]   | weight   | numeric   |
  +---------+----------+-----------+
  | [, 2]   | group    | factor    |
  +---------+----------+-----------+

  The levels of `group` are ‘ctrl’, ‘trt1’, and ‘trt2’.

  Dobson, A. J. (1983) *An Introduction to Statistical Modelling*. London:
  Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `plant_growth.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'plant_growth.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/PlantGrowth.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='plant_growth.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
