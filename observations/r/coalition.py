# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def coalition(path):
  """Coalition Dissolution in Parliamentary Democracies

  This data set contains survival data on government coalitions in
  parliamentary democracies (Belgium, Canada, Denmark, Finland, France,
  Iceland, Ireland, Israel, Italy, Netherlands, Norway, Portugal, Spain,
  Sweden, and the United Kingdom) for the period 1945-1987. For parsimony,
  country indicator variables are omitted in the sample data.

  A table containing 7 variables ("duration", "ciep12", "invest", "fract",
  "polar", "numst2", "crisis") and 314 observations. For variable
  descriptions, please refer to King, Alt, Burns and Laver (1990).

  ICPSR

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `coalition.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 314 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'coalition.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/Zelig/coalition.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='coalition.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
