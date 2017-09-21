# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def nidd_annual(path):
  """The River Nidd Data

  These data represent annual maximal levels of the River Nidd in
  Yorkshire. These data are suitable for analysis with `gev`.


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `nidd_annual.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 35 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'nidd_annual.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/evir/nidd.annual.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='nidd_annual.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
