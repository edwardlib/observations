# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def forbes(path):
  """Forbes' Data on Boiling Points in the Alps

  A data frame with 17 observations on boiling point of water and
  barometric pressure in inches of mercury.

  `bp`
      boiling point (degrees Farenheit).

  `pres`
      barometric pressure in inches of mercury.

  A. C. Atkinson (1985) *Plots, Transformations and Regression.* Oxford.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `forbes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 17 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'forbes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/forbes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='forbes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
