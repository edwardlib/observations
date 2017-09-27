# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def burt(path):
  """Fraudulent Data on IQs of Twins Raised Apart

  The `Burt` data frame has 27 rows and 4 columns. The “data” were
  simply (and notoriously) manufactured. The same data are in the dataset
  “twins" in the `alr3` package, but with different labels.

  This data frame contains the following columns:

  IQbio
      IQ of twin raised by biological parents

  IQfoster
      IQ of twin raised by foster parents

  class
      A factor with levels (note: out of order): `high`; `low`;
      `medium`.

  Burt, C. (1966) The genetic determination of differences in
  intelligence: A study of monozygotic twins reared together and apart.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `burt.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 27 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'burt.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Burt.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='burt.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
