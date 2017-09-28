# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def galton(path):
  """Galton's data on the heights of parents and their children

  Galton (1886) presented these data in a table, showing a
  cross-tabulation of 928 adult children born to 205 fathers and mothers,
  by their height and their mid-parent's height. He visually smoothed the
  bivariate frequency distribution and showed that the contours formed
  concentric and similar ellipses, thus setting the stage for correlation,
  regression and the bivariate normal distribution.

  A data frame with 928 observations on the following 2 variables.

  `parent`
      a numeric vector: height of the mid-parent (average of father and
      mother)

  `child`
      a numeric vector: height of the child

  Galton, F. (1886). Regression Towards Mediocrity in Hereditary Stature
  *Journal of the Anthropological Institute*, 15, 246-263

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `galton.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 898 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'galton.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Galton.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='galton.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
