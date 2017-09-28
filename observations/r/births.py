# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def births(path):
  """US Births

  Number of births each day from 1968 to 1988

  A data.frame with 7305 observations on the following 8 variables.

  itemcodedate [Date] itemcodebirths number of births on `date`
  [integer] itemcodewday day of week [ordered factor] itemcodeyear year
  [integer] itemcodemonth month [integer] itemcodeday day of month
  [integer] itemcodeday\_of\_year day of year [integer]
  itemcodeday\_of\_week day of week [integer]

  Data source: National Vital Statistics System natality data, as provided
  by Google BigQuery and exported to csv Robert Kern
  (http://www.mechanicalkern.com/static/birthdates-1968-1988.csv)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `births.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7305 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'births.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/mosaicData/Births.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='births.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
