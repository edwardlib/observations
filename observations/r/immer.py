# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def immer(path):
  """Yields from a Barley Field Trial

  The `immer` data frame has 30 rows and 4 columns. Five varieties of
  barley were grown in six locations in each of 1931 and 1932.

  This data frame contains the following columns:

  `Loc`
      The location.

  `Var`
      The variety of barley (`"manchuria"`, `"svansota"`,
      `"velvet"`, `"trebi"` and `"peatland"`).

  `Y1`
      Yield in 1931.

  `Y2`
      Yield in 1932.

  Immer, F.R., Hayes, H.D. and LeRoy Powers (1934) Statistical
  determination of barley varietal adaptation. *Journal of the American
  Society for Agronomy* **26**, 403–419.

  Fisher, R.A. (1947) *The Design of Experiments.* 4th edition. Edinburgh:
  Oliver and Boyd.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `immer.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 30 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'immer.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/immer.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='immer.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
