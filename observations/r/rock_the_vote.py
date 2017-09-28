# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def rock_the_vote(path):
  """Voter turnout experiment, using Rock The Vote ads

  Voter turnout data spanning 85 cable TV systems, randomly allocated to a
  voter mobilization experiment targetting 18-19 year olds with "Rock the
  Vote" television advertisments

  A data frame with 85 observations on the following 6 variables.

  `strata`
      numeric, experimental strata

  `treated`
      numeric, 1 if a treated cable system, 0 otherwise

  `r`
      numeric, number of 18 and 19 year olds turning out

  `n`
      numeric, number of 19 and 19 year olds registered

  `p`
      numeric, proportion of 18 and 19 year olds turning out

  `treatedIndex`
      numeric, a counter indexing the 42 treated units

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `rock_the_vote.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 85 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'rock_the_vote.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/RockTheVote.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='rock_the_vote.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
