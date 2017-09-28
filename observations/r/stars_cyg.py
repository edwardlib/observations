# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def stars_cyg(path):
  """Hertzsprung-Russell Diagram Data of Star Cluster CYG OB1

  Data for the Hertzsprung-Russell Diagram of the Star Cluster CYG OB1,
  which contains 47 stars in the direction of Cygnus, from C.Doom. The
  first variable is the logarithm of the effective temperature at the
  surface of the star (Te) and the second one is the logarithm of its
  light intencity (*L/L\_0*).

  | In the Hertzsprung-Russell diagram, which is the scatterplot of these
    data points, where the log temperature is plotted from left to right,
    two groups of points are seen:
  | the majority which tend to follow a steep band and four stars in the
    upper corner. In the astronomy the 43 stars are said to lie on the
    main sequence and the four remaining stars are called “giants” (the
    points 11, 20, 30, 34).

  A data frame with 47 observations on the following 2 variables

  `log.Te`
      Logarithm of the effective temperature at the surface of the star
      (Te).

  `log.light`
      Logarithm of its light intencity (*L/L\_0*)

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.27, table 3.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `stars_cyg.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 47 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'stars_cyg.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/starsCYG.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='stars_cyg.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
