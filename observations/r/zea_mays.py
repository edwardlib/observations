# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def zea_mays(path):
  """Darwin's Heights of Cross- and Self-fertilized Zea May Pairs

  Darwin (1876) studied the growth of pairs of zea may (aka corn)
  seedlings, one produced by cross-fertilization and the other produced by
  self-fertilization, but otherwise grown under identical conditions. His
  goal was to demonstrate the greater vigour of the cross-fertilized
  plants. The data recorded are the final height (inches, to the nearest
  1/8th) of the plants in each pair.

  In the *Design of Experiments*, Fisher (1935) used these data to
  illustrate a paired t-test (well, a one-sample test on the mean
  difference, `cross - self`). Later in the book (section 21), he used
  this data to illustrate an early example of a non-parametric permutation
  test, treating each paired difference as having (randomly) either a
  positive or negative sign.

  A data frame with 15 observations on the following 4 variables.

  `pair`
      pair number, a numeric vector

  `pot`
      pot, a factor with levels `1` `2` `3` `4`

  `cross`
      height of cross fertilized plant, a numeric vector

  `self`
      height of self fertilized plant, a numeric vector

  `diff`
      `cross - self` for each pair

  Darwin, C. (1876). *The Effect of Cross- and Self-fertilization in the
  Vegetable Kingdom*, 2nd Ed. London: John Murray.

  Andrews, D. and Herzberg, A. (1985) *Data: a collection of problems from
  many fields for the student and research worker*. New York: Springer.
  Data retrieved from: `https://www.stat.cmu.edu/StatDat/`

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `zea_mays.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 15 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'zea_mays.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/ZeaMays.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='zea_mays.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
