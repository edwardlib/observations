# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def anscombe(path):
  """Anscombe's Quartet of ‘Identical’ Simple Linear Regressions

  Four *x*-*y* datasets which have the same traditional statistical
  properties (mean, variance, correlation, regression line, etc.), yet are
  quite different.

  A data frame with 11 observations on 8 variables.

  +------------------+----------------------------------------------------+
  | x1 == x2 == x3   | the integers 4:14, specially arranged              |
  +------------------+----------------------------------------------------+
  | x4               | values 8 and 19                                    |
  +------------------+----------------------------------------------------+
  | y1, y2, y3, y4   | numbers in (3, 12.5) with mean 7.5 and sdev 2.03   |
  +------------------+----------------------------------------------------+

  Tufte, Edward R. (1989) *The Visual Display of Quantitative
  Information*, 13–14. Graphics Press.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `anscombe.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'anscombe.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/anscombe.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='anscombe.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
