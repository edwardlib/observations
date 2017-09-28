# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def hedonic(path):
  """Hedonic Prices of Census Tracts in Boston

  a cross-section

  *number of observations* : 506

  *observation* : regional

  *country* : United States

  A dataframe containing :

  mv
      median value of owner–occupied homes

  crim
      crime rate

  zn
      proportion of 25,000 square feet residential lots

  indus
      proportion of nonretail business acres

  chas
      is the tract bounds the Charles River ?

  nox
      annual average nitrogen oxide concentration in parts per hundred
      million

  rm
      average number of rooms

  age
      proportion of owner units built prior to 1940

  dis
      weighted distances to five employment centers in the Boston area

  rad
      index of accessibility to radial highways

  tax
      full value property tax rate (\\$/\\$10,000)

  ptratio
      pupil/teacher ratio

  blacks
      proportion of blacks in the population

  lstat
      proportion of population that is lower status

  townid
      town identifier

  Harrison, D. and D.L. Rubinfeld (1978) “Hedonic housing prices and the
  demand for clean air”, *Journal of Environmental Economics Ans
  Management*, **5**, 81–102.

  Belsley, D.A., E. Kuh and R. E. Welsch (1980) *Regression diagnostics:
  identifying influential data and sources of collinearity*, John Wiley,
  New–York.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `hedonic.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 506 rows and 15 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'hedonic.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Ecdat/Hedonic.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='hedonic.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
