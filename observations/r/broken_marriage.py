# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def broken_marriage(path):
  """Broken Marriage Data

  Data from the Danish Welfare Study about broken marriages or permanent
  relationships depending on gender and social rank.

  A data frame with 20 observations and 4 variables.

  Freq
      frequency.

  gender
      factor indicating gender (male, female).

  rank
      factor indicating social rank (I, II, III, IV, V).

  broken
      factor indicating whether the marriage or permanent relationship was
      broken (yes, no).

  E. B. Andersen (1991), The Statistical Analysis of Categorical Data,
  page 177.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `broken_marriage.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 20 rows and 4 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'broken_marriage.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/BrokenMarriage.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='broken_marriage.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
