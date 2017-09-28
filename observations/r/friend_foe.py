# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def friend_foe(path):
  """Data from the Television Game Show Friend Or Foe ?

  a cross-section from 2002–03

  *number of observations* : 227

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  sex
      contestant's sex

  white
      is contestant white ?

  age
      contestant's age in years

  play
      contestant's choice : a factor with levels "foe" and "friend". If
      both players play "friend", they share the trust box, if both play
      "foe", both players receive zero prize, if one of them play "foe"
      and the other one "friend", the "foe" player receive the entire
      trust bix and the "friend" player nothing

  round
      round in which contestant is eliminated, a factor with levels
      ("1","2","3")

  season
      season show, a factor with levels ("1","2")

  cash
      the amount of cash in the trust box

  sex1
      partner's sex

  white1
      is partner white ?

  age1
      partner's age in years

  play1
      partner's choice : a factor with levels "foe" and "friend"

  win
      money won by contestant

  win1
      money won by partner

  Kalist, David E. (2004) “Data from the Television Game Show "Friend or
  Foe?"”, *Journal of Statistics Education*, **12(3)**.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `friend_foe.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 227 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'friend_foe.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/FriendFoe.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='friend_foe.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
