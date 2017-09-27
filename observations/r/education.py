# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def education(path):
  """Education Expenditure Data

  Education Expenditure Data, from Chatterjee and Price (1977, p.108).
  This data set, representing the education expenditure variables in the
  50 US states, providing an interesting example of heteroscedacity.

  A data frame with 50 observations on the following 6 variables.

  `State`
      State

  `Region`
      Region (1=Northeastern, 2=North central, 3=Southern, 4=Western)

  `X1`
      Number of residents per thousand residing in urban areas in 1970

  `X2`
      Per capita personal income in 1973

  `X3`
      Number of residents per thousand under 18 years of age in 1974

  `Y`
      Per capita expenditure on public education in a state, projected for
      1975

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.110, table 16.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `education.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 6 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'education.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/education.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='education.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
