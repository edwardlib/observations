# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def butterfly(path):
  """Butterfly Species in Malaya

  Data from Fisher et al. (1943) giving the number of tokens found for
  each of 501 species of butterflies collected in Malaya.

  A 1-way table giving the number of tokens for 501 species of
  butterflies. The variable and its levels are

  No

  Name

  Levels

  1

  nTokens

  0, 1, ..., 24

  Michael Friendly (2000), Visualizing Categorical Data, pages 21–22.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `butterfly.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 24 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'butterfly.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/vcd/Butterfly.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='butterfly.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
