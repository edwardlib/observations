# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pearson_lee(path):
  """Pearson and Lee's data on the heights of parents and children classified b
  y gender

  Wachsmuth et. al (2003) noticed that a loess smooth through Galton's
  data on heights of mid-parents and their offspring exhibited a slightly
  non-linear trend, and asked whether this might be due to Galton having
  pooled the heights of fathers and mothers and sons and daughters in
  constructing his tables and graphs.

  To answer this question, they used analogous data from English families
  at about the same time, tabulated by Karl Pearson and Alice Lee (1896,
  1903), but where the heights of parents and children were each
  classified by gender of the parent.

  A frequency data frame with 746 observations on the following 6
  variables.

  `child`
      child height in inches, a numeric vector

  `parent`
      parent height in inches, a numeric vector

  `frequency`
      a numeric vector

  `gp`
      a factor with levels `fd` `fs` `md` `ms`

  `par`
      a factor with levels `Father` `Mother`

  `chl`
      a factor with levels `Daughter` `Son`

  Pearson, K. and Lee, A. (1896). Mathematical contributions to the theory
  of evolution. On telegony in man, etc. *Proceedings of the Royal Society
  of London*, 60 , 273-283.

  Pearson, K. and Lee, A. (1903). On the laws of inheritance in man: I.
  Inheritance of physical characters. *Biometika*, 2(4), 357-462. (Tables
  XXII, p. 415; XXV, p. 417; XXVIII, p. 419 and XXXI, p. 421.)

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pearson_lee.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 746 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pearson_lee.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/PearsonLee.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pearson_lee.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
