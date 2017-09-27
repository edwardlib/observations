# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def computers(path):
  """Prices of Personal Computers

  a cross-section from 1993 to 1995

  *number of observations* : 6259

  *observation* : goods

  *country* : United States

  A dataframe containing :

  price
      price in US dollars of 486 PCs

  speed
      clock speed in MHz

  hd
      size of hard drive in MB

  ram
      size of Ram in in MB

  screen
      size of screen in inches

  cd
      is a CD-ROM present ?

  multi
      is a multimedia kit (speakers, sound card) included ?

  premium
      is the manufacturer was a "premium" firm (IBM, COMPAQ) ?

  ads
      number of 486 price listings for each month

  trend
      time trend indicating month starting from January of 1993 to
      November of 1995.

  Stengos, T. and E. Zacharias (2005) “Intertemporal pricing and price
  discrimination : a semiparametric hedonic analysis of the personal
  computer market”, *Journal of Applied Econometrics*, **forthcoming**.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `computers.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 6259 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'computers.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Computers.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='computers.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
