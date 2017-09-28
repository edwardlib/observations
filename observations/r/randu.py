# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def randu(path):
  """Random Numbers from Congruential Generator RANDU

  400 triples of successive random numbers were taken from the VAX FORTRAN
  function RANDU running under VMS 1.5.

  A data frame with 400 observations on 3 variables named `x`, `y` and
  `z` which give the first, second and third random number in the
  triple.

  David Donoho

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `randu.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 400 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'randu.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/randu.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='randu.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
