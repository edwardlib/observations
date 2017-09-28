# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def sorption(path):
  """sorption data set

  Concentration-time measurements on different varieties of apples under
  methyl bromide injection.

  A data frame with 192 observations on the following 14 variables.

  m5
      a numeric vector

  m10
      a numeric vector

  m30
      a numeric vector

  m60
      a numeric vector

  m90
      a numeric vector

  m120
      a numeric vector

  ct
      concentration-time

  Cultivar
      a factor with levels `Pacific Rose` `BRAEBURN` `Fuji`
      `GRANNY` `Gala` `ROYAL` `Red Delicious` `Splendour`

  Dose
      injected dose of methyl bromide

  rep
      replicate number, within Cultivar and year

  year
      a factor with levels `1988` `1989` `1998` `1999`

  year.rep
      a factor with levels `1988:1` `1988:2` `1988:3` `1989:1`
      `1989:2` `1998:1` `1998:2` `1998:3` `1999:1` `1999:2`

  gp
      a factor with levels `BRAEBURN1` `BRAEBURN2` `Fuji1`
      `Fuji10` `Fuji2` `Fuji6` `Fuji7` `Fuji8` `Fuji9`
      `GRANNY1` `GRANNY2` `Gala4` `Gala5` `Pacific Rose10`
      `Pacific Rose6` `Pacific Rose7` `Pacific Rose8`
      `Pacific Rose9` `ROYAL1` `ROYAL2` `Red Del10` `Red Del9`
      `Red Delicious1` `Red Delicious2` `Red Delicious3`
      `Red Delicious4` `Red Delicious5` `Red Delicious6`
      `Red Delicious7` `Red Delicious8` `Splendour4` `Splendour5`

  inyear

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `sorption.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 192 rows and 14 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'sorption.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/sorption.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='sorption.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
