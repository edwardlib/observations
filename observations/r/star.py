# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def star(path):
  """Effects on Learning of Small Class Sizes

  a cross-section from 1985-89

  *number of observations* : 5748

  *observation* : individuals

  *country* : United States

  A dataframe containing :

  tmathssk
      total math scaled score

  treadssk
      total reading scaled score

  classk
      type of class, a factor with levels
      (regular,small.class,regular.with.aide)

  totexpk
      years of total teaching experience

  sex
      a factor with levels (boy,girl)

  freelunk
      qualified for free lunch ?

  race
      a factor with levels (white,black,other)

  schidkn
      school indicator variable

  Project STAR http://www.heros-inc.org/star.htm.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `star.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 5748 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'star.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Star.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='star.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
