# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def votes_repub(path):
  """Votes for Republican Candidate in Presidential Elections

  A data frame with the percents of votes given to the republican
  candidate in presidential elections from 1856 to 1976. Rows represent
  the 50 states, and columns the 31 elections.

  S. Peterson (1973): *A Statistical History of the American Presidential
  Elections*. New York: Frederick Ungar Publishing Co.

  Data from 1964 to 1976 is from R. M. Scammon, *American Votes 12*,

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `votes_repub.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 31 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'votes_repub.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/votes.repub.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='votes_repub.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
