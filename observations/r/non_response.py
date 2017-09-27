# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def non_response(path):
  """Non-Response Survey Data

  Data about non-response for a Danish survey in 1965.

  A data frame with 12 observations and 4 variables.

  Freq
      frequency.

  residence
      factor indicating whether residence was in Copenhagen, in a city
      outside Copenhagen or at the countryside (Copenhagen, City,
      Country).

  response
      factor indicating whether a response was given (yes, no).

  gender
      factor indicating gender (male, female).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  Table 5.17.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `non_response.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'non_response.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/NonResponse.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='non_response.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
