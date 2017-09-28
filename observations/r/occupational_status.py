# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def occupational_status(path):
  """Occupational Status of Fathers and their Sons

  Cross-classification of a sample of British males according to each
  subject's occupational status and his father's occupational status.

  A `table` of counts, with classifying factors `origin` (father's
  occupational status; levels `1:8`) and `destination` (son's
  occupational status; levels `1:8`).

  Goodman, L. A. (1979) Simple Models for the Analysis of Association in
  Cross-Classifications having Ordered Categories. *J. Am. Stat. Assoc.*,
  **74** (367), 537–552.

  The data set has been in package
  `gnm <https://CRAN.R-project.org/package=gnm>`__ and been provided by
  the package authors.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `occupational_status.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 8 rows and 8 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'occupational_status.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/datasets/occupationalStatus.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='occupational_status.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
