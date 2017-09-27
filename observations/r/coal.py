# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def coal(path):
  """Dates of Coal Mining Disasters

  The `coal` data frame has 191 rows and 1 columns.

  This data frame gives the dates of 191 explosions in coal mines which
  resulted in 10 or more fatalities. The time span of the data is from
  March 15, 1851 until March 22 1962.

  This data frame contains the following column:

  `date`
      The date of the disaster. The integer part of `date` gives the
      year. The day is represented as the fraction of the year that had
      elapsed on that day.

  The data were obtained from

  Hand, D.J., Daly, F., Lunn, A.D., McConway, K.J. and Ostrowski, E.
  (1994) *A Handbook of Small Data Sets*, Chapman and Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `coal.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 191 rows and 1 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'coal.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/coal.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='coal.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
