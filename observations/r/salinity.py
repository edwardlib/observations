# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def salinity(path):
  """Water Salinity and River Discharge

  The `salinity` data frame has 28 rows and 4 columns.

  Biweekly averages of the water salinity and river discharge in Pamlico
  Sound, North Carolina were recorded between the years 1972 and 1977. The
  data in this set consists only of those measurements in March, April and
  May.

  This data frame contains the following columns:

  `sal`
      The average salinity of the water over two weeks.

  `lag`
      The average salinity of the water lagged two weeks. Since only
      spring is used, the value of `lag` is not always equal to the
      previous value of `sal`.

  `trend`
      A factor indicating in which of the 6 biweekly periods between March
      and May, the observations were taken. The levels of the factor are
      from 0 to 5 with 0 being the first two weeks in March.

  `dis`
      The amount of river discharge during the two weeks for which `sal`
      is the average salinity.

  The data were obtained from

  Ruppert, D. and Carroll, R.J. (1980) Trimmed least squares estimation in
  the linear model. *Journal of the American Statistical Association*,
  **75**, 828–838.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `salinity.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 28 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'salinity.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/salinity.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='salinity.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
