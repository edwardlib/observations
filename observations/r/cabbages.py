# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cabbages(path):
  """Data from a cabbage field trial

  The `cabbages` data set has 60 observations and 4 variables

  This data frame contains the following columns:

  `Cult`
      Factor giving the cultivar of the cabbage, two levels: `c39` and
      `c52`.

  `Date`
      Factor specifying one of three planting dates: `d16`, `d20` or
      `d21`.

  `HeadWt`
      Weight of the cabbage head, presumably in kg.

  `VitC`
      Ascorbic acid content, in undefined units.

  Rawlings, J. O. (1988) *Applied Regression Analysis: A Research Tool.*
  Wadsworth and Brooks/Cole. Example 8.4, page 219. (Rawlings cites the
  original source as the files of the late Dr Gertrude M Cox.)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cabbages.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cabbages.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/cabbages.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cabbages.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
