# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sunspot_month(path):
  """Monthly Sunspot Data, from 1749 to "Present"

  Monthly numbers of sunspots, as from the World Data Center, aka SIDC.
  This is the version of the data that will occasionally be updated when
  new counts become available.

  The univariate time series `sunspot.year` and `sunspot.month`
  contain 289 and 2988 observations, respectively. The objects are of
  class `"ts"`.

  Author(s)
  ~~~~~~~~~

  R

  WDC-SILSO, Solar Influences Data Analysis Center (SIDC), Royal
  Observatory of Belgium, Av. Circulaire, 3, B-1180 BRUSSELS Currently at
  http://www.sidc.be/silso/datafiles

  See Also
  ~~~~~~~~

  `sunspot.month` is a longer version of `sunspots`; the latter runs
  until 1983 and is kept fixed (for reproducibility as example dataset).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sunspot_month.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3177 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sunspot_month.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/sunspot.month.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sunspot_month.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
