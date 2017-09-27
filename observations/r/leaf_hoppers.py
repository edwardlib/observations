# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def leaf_hoppers(path):
  """LeafHoppers

  Lefetimes for potato leafhoppers on various sugar diets

  A dataset with 8 observations on the following 2 variables.

  `Diet`

  `Control`, `Fructose`, `Glucose`, or `Sucrose`

  `Days`

  Number of days until half the leafhoppers in a dish died

  "Survival and behavioral responses of the potato leafhopper, Empoasca
  Fabae (Harris), on synthetic media," MS thesis by Douglas Dahlman
  (1963), Iowa State University. The data can be found in Analyzing
  Experimental Data by Regression by David M. Allen and Foster B. Cady,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `leaf_hoppers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'leaf_hoppers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/LeafHoppers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='leaf_hoppers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
