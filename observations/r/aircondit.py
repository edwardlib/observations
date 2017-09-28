# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aircondit(path):
  """Failures of Air-conditioning Equipment

  Proschan (1963) reported on the times between failures of the
  air-conditioning equipment in 10 Boeing 720 aircraft. The `aircondit`
  data frame contains the intervals for the ninth aircraft while
  `aircondit7` contains those for the seventh aircraft.

  Both data frames have just one column. Note that the data have been
  sorted into increasing order.

  The data frames contain the following column:

  `hours`
      The time interval in hours between successive failures of the
      air-conditioning equipment

  The data were taken from

  Cox, D.R. and Snell, E.J. (1981) *Applied Statistics: Principles and
  Examples*. Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aircondit.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aircondit.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/aircondit.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aircondit.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
