# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def women_queue(path):
  """Women in Queues

  Data from Jinkinson \\& Slater (1981) and Hoaglin \\& Tukey (1985)
  reporting the frequency distribution of females in 100 queues of length
  10 in a London Underground station.

  A 1-way table giving the number of women in 100 queues of length 10. The
  variable and its levels are

  No

  Name

  Levels

  1

  nWomen

  0, 1, ..., 10

  M. Friendly (2000), Visualizing Categorical Data, pages 19–20.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `women_queue.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 11 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'women_queue.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/WomenQueue.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='women_queue.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
