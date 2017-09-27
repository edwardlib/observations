# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def aircraft(path):
  """Aircraft Data

  Aircraft Data, deals with 23 single-engine aircraft built over the years
  1947-1979, from Office of Naval Research. The dependent variable is cost
  (in units of \\$100,000) and the explanatory variables are aspect ratio,
  lift-to-drag ratio, weight of plane (in pounds) and maximal thrust.

  A data frame with 23 observations on the following 5 variables.

  `X1`
      Aspect Ratio

  `X2`
      Lift-to-Drag Ratio

  `X3`
      Weight

  `X4`
      Thrust

  `Y`
      Cost

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, page 154, table 22.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `aircraft.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 23 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'aircraft.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/aircraft.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='aircraft.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
