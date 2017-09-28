# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def xclara(path):
  """Bivariate Data Set with 3 Clusters

  An artificial data set consisting of 3000 points in 3 well-separated
  clusters of size 1000 each.

  A data frame with 3000 observations on 2 numeric variables giving the
  *x* and *y* coordinates of the points, respectively.

  Sample data set accompanying the reference below.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `xclara.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3000 rows and 2 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'xclara.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/cluster/xclara.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='xclara.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
