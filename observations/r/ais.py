# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ais(path):
  """Australian athletes data set

  These data were collected in a study of how data on various
  characteristics of the bloood varied with sport body size and sex of the
  athlete.

  A data frame with 202 observations on the following 13 variables.

  rcc
      red blood cell count, in **

  wcc
      while blood cell count, in ** per liter

  hc
      hematocrit, percent

  hg
      hemaglobin concentration, in g per decaliter

  ferr
      plasma ferritins, ng **

  bmi
      Body mass index, kg **

  ssf
      sum of skin folds

  pcBfat
      percent Body fat

  lbm
      lean body mass, kg

  ht
      height, cm

  wt
      weight, kg

  sex
      a factor with levels `f` `m`

  sport
      a factor with levels `B_Ball` `Field` `Gym` `Netball`
      `Row` `Swim` `T_400m` `T_Sprnt` `Tennis` `W_Polo`

  These data were the basis for the analyses that are reported in Telford
  and Cunningham (1991).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ais.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 202 rows and 13 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ais.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/DAAG/ais.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ais.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
