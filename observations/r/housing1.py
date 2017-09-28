# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def housing1(path):
  """Frequency Table from a Copenhagen Housing Conditions Survey

  The `housing` data frame has 72 rows and 5 variables.

  `Sat`
      Satisfaction of householders with their present housing
      circumstances, (High, Medium or Low, ordered factor).

  `Infl`
      Perceived degree of influence householders have on the management of
      the property (High, Medium, Low).

  `Type`
      Type of rental accommodation, (Tower, Atrium, Apartment, Terrace).

  `Cont`
      Contact residents are afforded with other residents, (Low, High).

  `Freq`
      Frequencies: the numbers of residents in each class.

  Madsen, M. (1976) Statistical analysis of multiple contingency tables.
  Two examples. *Scand. J. Statist.* **3**, 97–106.

  Cox, D. R. and Snell, E. J. (1984) *Applied Statistics, Principles and
  Examples*. Chapman & Hall.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `housing1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1448 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'housing1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/housing.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='housing1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
