# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def coal_miners(path):
  """Breathlessness and Wheeze in Coal Miners

  Data from Ashford & Sowden (1970) given by Agresti (1990) on the
  association between two pulmonary conditions, breathlessness and wheeze,
  in a large sample of coal miners who were smokers with no radiological
  evidence of pneumoconlosis, aged between 20–64 when examined. This data
  is frequently used as an example of fitting models for bivariate, binary
  responses.

  A 3-dimensional table of size 2 x 2 x 9 resulting from cross-tabulating
  variables for 18,282 coal miners. The variables and their levels are as
  follows:

  +------+------------------+-----------------------------------+
  | No   | Name             | Levels                            |
  +------+------------------+-----------------------------------+
  | 1    | Breathlessness   | B, NoB                            |
  +------+------------------+-----------------------------------+
  | 2    | Wheeze           | W, NoW                            |
  +------+------------------+-----------------------------------+
  | 3    | Age              | 20-24, 25-29, 30-34, ..., 60-64   |
  +------+------------------+-----------------------------------+

  Michael Friendly (2000), Visualizing Categorical Data, pages 82–83,
  319–322.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `coal_miners.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 36 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'coal_miners.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/CoalMiners.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='coal_miners.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
