# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sunspots(path):
  """Monthly Sunspot Numbers, 1749–1983

  Monthly mean relative sunspot numbers from 1749 to 1983. Collected at
  Swiss Federal Observatory, Zurich until 1960, then Tokyo Astronomical
  Observatory.

  A time series of monthly data from 1749 to 1983.

  Andrews, D. F. and Herzberg, A. M. (1985) *Data: A Collection of
  Problems from Many Fields for the Student and Research Worker*. New
  York: Springer-Verlag.

  See Also
  ~~~~~~~~

  `sunspot.month` has a longer (and a bit different) series,
  `sunspot.year` is a much shorter one. See there for getting more
  current sunspot numbers.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sunspots.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2820 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sunspots.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/sunspots.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sunspots.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
