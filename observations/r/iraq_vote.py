# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def iraq_vote(path):
  """U.S. Senate vote on the use of force against Iraq, 2002.

  On October 11, 2002, the United States Senate voted 77-23 to authorize
  the use of military force against Iraq. This data set lists the “Ayes”
  and “Nays” for each Senator and some covariates.

  A data frame with 100 observations on the following 6 variables.

  `y`
      a numeric vector, the recorded vote (1 if Aye, 0 if Nay)

  `state.abb`
      two letter abbreviation for each state

  `name`
      senator name, party and state, e.g., `AKAKA (D HI)`

  `rep`
      logical, `TRUE` for Republican senators

  `state.name`
      name of state

  `gorevote`
      numeric, the vote share recorded by Al Gore in the corresponding
      state in the 2000 Presidential election

  Keith Poole, 107th Senate Roll Call Data.
  ftp://voteview.com/sen107kh.ord The Iraq vote is vote number 617.

  David Leip's Atlas of U.S. Presidential Elections.
  http://uselectionatlas.org

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `iraq_vote.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 100 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'iraq_vote.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/pscl/iraqVote.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='iraq_vote.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
