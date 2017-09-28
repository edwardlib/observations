# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def gorsuch(path):
  """Example data set from Gorsuch (1997) for an example factor extension.

  Gorsuch (1997) suggests an alternative to the classic Dwyer (1937)
  factor extension technique. This data set is taken from that article.
  Useful for comparing `link{fa.extension}` with and without the
  correct=TRUE option.

  Richard L. Gorsuch (1997) New Procedure for Extension Analysis in
  Exploratory Factor Analysis. Educational and Psychological Measurement,
  57, 725-740.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `gorsuch.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 10 rows and 10 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'gorsuch.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/Gorsuch.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='gorsuch.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
