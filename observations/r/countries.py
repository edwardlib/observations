# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def countries(path):
  """Countries

  A data frame containing country names as used by GapMinder and the
  `maps` package to facilitate converstion between the two.

  A data frame with 258 observations on the following variables.

  -  `worldmap` region name http://mappinghacks.com/ data sets

  -  `gapminder` country name in GapMinder data sets

  -  `maps` region name in `maps` data sets

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `countries.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 288 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'countries.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Countries.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='countries.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
