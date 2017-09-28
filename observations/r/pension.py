# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def pension(path):
  """Pension Funds Data

  The total 1981 premium income of pension funds of Dutch firms, for 18
  Professional Branches, from de Wit (1982).

  A data frame with 18 observations on the following 2 variables.

  `Income`
      Premium Income (in millions of guilders)

  `Reserves`
      Premium Reserves (in millions of guilders)

  P. J. Rousseeuw and A. M. Leroy (1987) *Robust Regression and Outlier
  Detection*; Wiley, p.76, table 13.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `pension.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 194 rows and 19 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'pension.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/robustbase/pension.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='pension.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
