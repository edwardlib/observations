# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def cattell(path):
  """12 cognitive variables from Cattell (1963)

  Rindskopf and Rose (1988) use this data set to demonstrate confirmatory
  second order factor models. It is a nice example data set to explore
  hierarchical structure and alternative factor solutions. It contains
  measures of fluid and crystallized intelligence.

  The format is: num [1:12, 1:12] 1 0.86 0.3 0.32 0.41 0.42 0.34 0.32 0.29
  0.21 ... - attr(\*, "dimnames")=List of 2 ..$ : chr [1:12] "Verbal"
  "Verbal2" "Space1" "Space2" ... ..$ : chr [1:12] "Verbal" "Verbal2"
  "Space1" "Space2" ...

  David Rindskopf and Tedd Rose, (1988) Some Theory and Applications of
  Confirmatory Second- Order Factor Analysis, Multivariate Behavioral
  Research, 23, 51-67.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `cattell.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 12 rows and 12 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'cattell.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/cattell.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='cattell.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
