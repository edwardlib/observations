# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def faithful(path):
  """Old Faithful Geyser Data

  Waiting time between eruptions and the duration of the eruption for the
  Old Faithful geyser in Yellowstone National Park, Wyoming, USA.

  A data frame with 272 observations on 2 variables.

  [,1]

  eruptions

  numeric

  Eruption time in mins

  [,2]

  waiting

  numeric

  Waiting time to next eruption (in mins)

  W. Härdle.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `faithful.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 272 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'faithful.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/faithful.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='faithful.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
