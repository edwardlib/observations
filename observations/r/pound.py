# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pound(path):
  """Pound-dollar Exchange Rate

  weekly observations from 1975 to 1989

  *number of observations* : 778

  *observation* : country

  *country* : Germany

  A dataframe containing :

  date
      the date of the observation (19850104 is January, 4, 1985)

  s
      the ask price of the dollar in units of Pound in the spot market on
      friday of the current week

  f
      the ask price of the dollar in units of Pound in the 30-day forward
      market on friday of the current week

  s30
      the bid price of the dollar in units of Pound in the spot market on
      the delivery date on a current forward contract

  Bekaert, G. and R. Hodrick (1993) “On biases in the measurement of
  foreign exchange risk premiums”, *Journal of International Money and
  Finance*, **12**, 115-138.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pound.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 778 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pound.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Pound.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pound.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
