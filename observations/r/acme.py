# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def acme(path):
  """Monthly Excess Returns

  The `acme` data frame has 60 rows and 3 columns.

  The excess return for the Acme Cleveland Corporation are recorded along
  with those for all stocks listed on the New York and American Stock
  Exchanges were recorded over a five year period. These excess returns
  are relative to the return on a risk-less investment such a U.S.
  Treasury bills.

  This data frame contains the following columns:

  `month`
      A character string representing the month of the observation.

  `market`
      The excess return of the market as a whole.

  `acme`
      The excess return for the Acme Cleveland Corporation.

  The data were obtained from

  Simonoff, J.S. and Tsai, C.-L. (1994) Use of modified profile likelihood
  for improved tests of constancy of variance in regression. *Applied
  Statistics*, **43**, 353–370.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `acme.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 60 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'acme.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/boot/acme.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='acme.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
