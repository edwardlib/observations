# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cpus(path):
  """Performance of Computer CPUs

  A relative performance measure and characteristics of 209 CPUs.

  The components are:

  `name`
      manufacturer and model.

  `syct`
      cycle time in nanoseconds.

  `mmin`
      minimum main memory in kilobytes.

  `mmax`
      maximum main memory in kilobytes.

  `cach`
      cache size in kilobytes.

  `chmin`
      minimum number of channels.

  `chmax`
      maximum number of channels.

  `perf`
      published performance on a benchmark mix relative to an IBM
      370/158-3.

  `estperf`
      estimated performance (by Ein-Dor & Feldmesser).

  P. Ein-Dor and J. Feldmesser (1987) Attributes of the performance of
  central processing units: a relative performance prediction model.
  *Comm. ACM.* **30**, 308–317.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cpus.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 209 rows and 9 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cpus.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/cpus.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cpus.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
