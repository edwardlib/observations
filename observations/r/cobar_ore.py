# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cobar_ore(path):
  """Cobar Ore data

  Cobar Ore data from Green and Silverman (1994). The data consists of
  measurements on the "true width" of an ore-bearing rock layer from a
  mine in Cobar, Australia.

  A data frame with 38 observations on the following 3 variables.

  x
      x-coordinate of location of mine site

  y
      y-coordinate of location of mine site

  z
      ore thickness

  Green, P.J. and B.W. Silverman (1994) Nonparametric Regression
  Generalized Linear Models: A roughness penalty approach, Chapman Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cobar_ore.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 38 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cobar_ore.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/quantreg/CobarOre.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cobar_ore.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
