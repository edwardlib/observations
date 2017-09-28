# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cavendish(path):
  """Cavendish's Determinations of the Density of the Earth

  Henry Cavendish carried out a series of experiments in 1798 to determine
  the mean density of the earth, as an indirect means to calculate the
  gravitational constant, G, in Newton's formula for the force (f) of
  gravitational attraction, *f = G m M / r^2* between two bodies of mass m
  and M.

  Stigler (1977) used these data to illustrate properties of robust
  estimators with real, historical data. For these data sets, he found
  that trimmed means performed as well or better than more elaborate
  robust estimators.

  A data frame with 29 observations on the following 3 variables.

  `density`
      Cavendish's 29 determinations of the mean density of the earth

  `density2`
      same as `density`, with the third value (4.88) replaced by 5.88

  `density3`
      same as `density`, omitting the the first 6 observations

  Kyle Siegrist, "Virtual Laboratories in Probability and Statistics",
  http://www.math.uah.edu/stat/data/Cavendish.html

  Stephen M. Stigler (1977), "Do robust estimators work with *real*
  data?", *Annals of Statistics*, 5, 1055-1098

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cavendish.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 29 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cavendish.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HistData/Cavendish.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cavendish.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
