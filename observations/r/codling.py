# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def codling(path):
  """Dose-mortality data, for fumigation of codling moth with methyl bromide

  Data are from trials that studied the mortality response of codling moth
  to fumigation with methyl bromide.

  A data frame with 99 observations on the following 10 variables.

  dose
      Injected dose of methyl bromide, in gm per cubic meter

  tot
      Number of insects in chamber

  dead
      Number of insects dying

  pobs
      Proportion dying

  cm
      Control mortality, i.e., at dose 0

  ct
      Concentration-time sum

  Cultivar
      a factor with levels `BRAEBURN` `FUJI` `GRANNY` `Gala`
      `ROYAL` `Red Delicious` `Splendour`

  gp
      a factor which has a different level for each different combination
      of `Cultivar`, `year` and `rep` (replicate).

  year
      a factor with levels `1988` `1989`

  numcm
      a numeric vector: total number of control insects

  Maindonald, J.H.; Waddell, B.C.; Petry, R.J. 2001. Apple cultivar
  effects on codling moth (Lepidoptera: Tortricidae) egg mortality
  following fumigation with methyl bromide. Postharvest Biology and

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `codling.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 99 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'codling.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/codling.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='codling.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
