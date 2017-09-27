# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def manitoba_lakes(path):
  """The Nine Largest Lakes in Manitoba

  The `Manitoba.lakes` data frame has 9 rows and 2 columns. The areas
  and elevations of the nine largest lakes in Manitoba, Canada. The
  geography of Manitoba (a relatively flat province) can be divided
  crudely into three main areas: a very flat prairie in the south which is
  at a relatively high elevation, a middle region consisting of mainly of
  forest and Precambrian rock, and a northern region which drains more
  rapidly into Hudson Bay. All water in Manitoba, which does not
  evaporate, eventually drains into Hudson Bay.

  This data frame contains the following columns:

  elevation
      a numeric vector consisting of the elevations of the lakes (in
      meters)

  area
      a numeric vector consisting of the areas of the lakes (in square
      kilometers)

  The CANSIM data base at Statistics Canada.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `manitoba_lakes.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 9 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'manitoba_lakes.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/Manitoba.lakes.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='manitoba_lakes.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
