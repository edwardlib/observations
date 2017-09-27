# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def galton1(path):
  """Galton's Mid parent child height data

  Two of the earliest examples of the correlation coefficient were Francis
  Galton's data sets on the relationship between mid parent and child
  height and the similarity of parent generation peas with child peas.
  This is the data set for the Galton height.

  A data frame with 928 observations on the following 2 variables.

  `parent`
      Mid Parent heights (in inches)

  `child`
      Child Height

  This is just the galton data set from UsingR, slightly rearranged.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `galton1.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 928 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'galton1.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/galton.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='galton1.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
