# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def world_phones(path):
  """The World's Telephones

  The number of telephones in various regions of the world (in thousands).

  A matrix with 7 rows and 8 columns. The columns of the matrix give the
  figures for a given region, and the rows the figures for a year.

  The regions are: North America, Europe, Asia, South America, Oceania,
  Africa, Central America.

  The years are: 1951, 1956, 1957, 1958, 1959, 1960, 1961.

  AT&T (1961) *The World's Telephones*.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `world_phones.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'world_phones.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/WorldPhones.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='world_phones.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
