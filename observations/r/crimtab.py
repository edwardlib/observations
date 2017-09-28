# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def crimtab(path):
  """Student's 3000 Criminals Data

  Data of 3000 male criminals over 20 years old undergoing their sentences
  in the chief prisons of England and Wales.

  A `table` object of `integer` counts, of dimension *42 \* 22* with a
  total count, `sum(crimtab)` of 3000.

  The 42 `rownames` (`"9.4"`, `"9.5"`, ...) correspond to midpoints
  of intervals of finger lengths whereas the 22 column names
  (`colnames`) (`"142.24"`, `"144.78"`, ...) correspond to (body)
  heights of 3000 criminals, see also below.

  http://pbil.univ-lyon1.fr/R/donnees/criminals1902.txt thanks to Jean R.
  Lobry and Anne-Béatrice Dufour.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `crimtab.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 42 rows and 22 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'crimtab.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/crimtab.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='crimtab.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
