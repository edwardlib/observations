# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def life_cycle_savings(path):
  """Intercountry Life-Cycle Savings Data

  Data on the savings ratio 1960–1970.

  A data frame with 50 observations on 5 variables.

  +--------+---------+-----------+-------------------------------------+
  | [,1]   | sr      | numeric   | aggregate personal savings          |
  +--------+---------+-----------+-------------------------------------+
  | [,2]   | pop15   | numeric   | % of population under 15            |
  +--------+---------+-----------+-------------------------------------+
  | [,3]   | pop75   | numeric   | % of population over 75             |
  +--------+---------+-----------+-------------------------------------+
  | [,4]   | dpi     | numeric   | real per-capita disposable income   |
  +--------+---------+-----------+-------------------------------------+
  | [,5]   | ddpi    | numeric   | % growth rate of dpi                |
  +--------+---------+-----------+-------------------------------------+

  The data were obtained from Belsley, Kuh and Welsch (1980). They in turn
  obtained the data from Sterling (1977).

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `life_cycle_savings.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 50 rows and 5 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'life_cycle_savings.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/LifeCycleSavings.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='life_cycle_savings.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
