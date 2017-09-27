# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tip_joke(path):
  """Tip Joke

  Effect of a waiter leaving a joke or an advertisement on getting a tip

  A dataset with 211 observations on the following 5 variables.

  `Card`

  Type of card used: `Ad`, `Joke`, or `None`

  `Tip`

  `1`\ =customer left a tip or `0`\ =no tip

  `Ad`

  Indicator for `Ad` card

  `Joke`

  Indicator for `Joke` card

  `None`

  Indicator for no card

  Gueguen, Nicholas (2002), "The Effects of a Joke on Tipping When it is
  Delivered at the Same Time as the Bill," Journal of Applied Social

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tip_joke.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 211 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tip_joke.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Stat2Data/TipJoke.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tip_joke.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
