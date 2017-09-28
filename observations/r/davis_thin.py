# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def davis_thin(path):
  """Davis's Data on Drive for Thinness

  The `DavisThin` data frame has 191 rows and 7 columns. This is part of
  a larger dataset for a study of eating disorders. The seven variables in
  the data frame comprise a "drive for thinness" scale, to be formed by
  summing the items.

  This data frame contains the following columns:

  DT1
      a numeric vector

  DT2
      a numeric vector

  DT3
      a numeric vector

  DT4
      a numeric vector

  DT5
      a numeric vector

  DT6
      a numeric vector

  DT7
      a numeric vector

  Davis, C., G. Claridge, and D. Cerullo (1997) Personality factors
  predisposing to weight preoccupation: A continuum approach to the
  association between eating disorders and personality disorders. *Journal
  of Psychiatric Research* **31**, 467–480. [personal communication from
  the authors.]

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `davis_thin.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 191 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'davis_thin.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/car/DavisThin.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='davis_thin.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
