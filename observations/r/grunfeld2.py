# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def grunfeld2(path):
  """Simulation Data for model Seemingly Unrelated Regression (sur) that corres
  ponds to method SUR of systemfit

  Dataframe contains 20 annual observations from 1935 to 1954 of 7
  variables for two firms General Electric and Westinghouse. Columns are
  Year; Ige and Iw = Gross investment for GE and W,respectively; Fge and
  Fw=Market value of Firm as of begin of the year; Cge and Cw= Capital
  stock measure as of begin of the year.

  A table containing 7 variables ("Year", "Ige", "Fge", "Cge","Iw",

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `grunfeld2.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'grunfeld2.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/grunfeld.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='grunfeld2.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
