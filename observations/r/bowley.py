# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def bowley(path):
  """Bowley's data on values of British and Irish trade, 1855-1899

  In one of the first statistical textbooks, Arthur Bowley (1901) used
  these data to illustrate an arithmetic and graphical analysis of
  time-series data using the total value of British and Irish exports from
  1855-1899. He presented a line graph of the time-series data,
  supplemented by overlaid line graphs of 3-, 5- and 10-year moving
  averages. His goal was to show that while the initial series showed wide
  variability, moving averages made the series progressively smoother.

  A data frame with 45 observations on the following 2 variables.

  `Year`
      Year, from 1855-1899

  `Value`
      total value of British and Irish exports (millions of Pounds)

  Bowley, A. L. (1901). *Elements of Statistics*. London: P. S. King and
  Son, p. 151-154.

  Digitized from Bowley's graph.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `bowley.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'bowley.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Bowley.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='bowley.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
