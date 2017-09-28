# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def chile(path):
  """Voting Intentions in the 1988 Chilean Plebiscite

  The `Chile` data frame has 2700 rows and 8 columns. The data are from
  a national survey conducted in April and May of 1988 by FLACSO/Chile.
  There are some missing data.

  This data frame contains the following columns:

  region
      A factor with levels: `C`, Central; `M`, Metropolitan Santiago
      area; `N`, North; `S`, South; `SA`, city of Santiago.

  population
      Population size of respondent's community.

  sex
      A factor with levels: `F`, female; `M`, male.

  age
      in years.

  education
      A factor with levels (note: out of order): `P`, Primary; `PS`,
      Post-secondary; `S`, Secondary.

  income
      Monthly income, in Pesos.

  statusquo
      Scale of support for the status-quo.

  vote
      a factor with levels: `A`, will abstain; `N`, will vote no
      (against Pinochet); `U`, undecided; `Y`, will vote yes (for
      Pinochet).

  Personal communication from FLACSO/Chile.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `chile.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 2700 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'chile.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Chile.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='chile.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
