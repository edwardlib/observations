# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def weimar(path):
  """1932 Weimar election data

  This data set contains election results for 10 kreise (equivalent to
  precincts) from the 1932 Weimar (German) election.

  A table containing 11 variables and 10 observations. The variables are

  Nazi
      Number of votes for the Nazi party

  Government
      Number of votes for the Government

  Communists
      Number of votes for the Communist party

  FarRight
      Number of votes for far right parties

  Other
      Number of votes for other parties, and non-voters

  shareunemployed
      Proportion unemployed

  shareblue
      Proportion working class

  sharewhite
      Proportion white-collar workers

  sharedomestic
      Proportion domestic servants

  shareprotestants
      Proportion Protestant


  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `weimar.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'weimar.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/Weimar.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='weimar.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
