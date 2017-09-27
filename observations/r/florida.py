# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def florida(path):
  """Florida County Voting

  The `Florida` data frame has 67 rows and 11 columns. Vote by county in
  Florida for President in the 2000 election.

  This data frame contains the following columns:

  GORE
      Number of votes for Gore

  BUSH
      Number of votes for Bush.

  BUCHANAN
      Number of votes for Buchanan.

  NADER
      Number of votes for Nader.

  BROWNE
      Number of votes for Browne (whoever that is).

  HAGELIN
      Number of votes for Hagelin (whoever that is).

  HARRIS
      Number of votes for Harris (whoever that is).

  MCREYNOLDS
      Number of votes for McReynolds (whoever that is).

  MOOREHEAD
      Number of votes for Moorehead (whoever that is).

  PHILLIPS
      Number of votes for Phillips (whoever that is).

  Total
      Total number of votes.

  Adams, G. D. and Fastnow, C. F. (2000) A note on the voting
  irregularities in Palm Beach, FL. Formerly at

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `florida.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 67 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'florida.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Florida.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='florida.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
