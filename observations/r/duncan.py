# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def duncan(path):
  """Duncan's Occupational Prestige Data

  The `Duncan` data frame has 45 rows and 4 columns. Data on the
  prestige and other characteristics of 45 U. S. occupations in 1950.

  This data frame contains the following columns:

  type
      Type of occupation. A factor with the following levels: `prof`,
      professional and managerial; `wc`, white-collar; `bc`,
      blue-collar.

  income
      Percent of males in occupation earning $3500 or more in 1950.

  education
      Percent of males in occupation in 1950 who were high-school
      graduates.

  prestige
      Percent of raters in NORC study rating occupation as excellent or
      good in prestige.

  Duncan, O. D. (1961) A socioeconomic index for all occupations. In
  Reiss, A. J., Jr. (Ed.) *Occupations and Social Status.* Free Press
  [Table VI-1].

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `duncan.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 45 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'duncan.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/Duncan.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='duncan.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
