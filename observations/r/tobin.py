# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def tobin(path):
  """Tobin's Tobit data

  Economists fit a parametric censored data model called the ‘tobit’.
  These data are from Tobin's original paper.

  A data frame with 20 observations on the following 3 variables.

  durable
      Durable goods purchase

  age
      Age in years

  quant
      Liquidity ratio (x 1000)

  J Tobin (1958), Estimation of relationships for limited dependent
  variables. *Econometrica* **26**, 24–36.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `tobin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'tobin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/tobin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='tobin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
